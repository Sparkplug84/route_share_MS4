from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Route, BikeType, RouteType
from .forms import RouteForm
from profiles.models import UserProfile


def all_routes(request):
    """ A view to show all routes, including sorting and search queries """

    routes = Route.objects.all()
    query = None
    biketypes = None
    countries = None
    route_types = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                routes = routes.annotate(lower_name=Lower('name'))
            if sortkey == 'bike_type':
                sortkey = 'bike_type__name'
            if sortkey == 'route_type':
                sortkey = 'route_type__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            routes = routes.order_by(sortkey)
            if sortkey == 'country':
                routes = sorted(routes, key=lambda route: route.country.name)
            if sortkey == '-country':
                routes = sorted(
                    routes, key=lambda route: route.country.name, reverse=True)

        if 'bike_type' in request.GET:
            biketypes = request.GET['bike_type'].split(',')
            routes = routes.filter(bike_type__name__in=biketypes)
            biketypes = BikeType.objects.filter(name__in=biketypes)

        if 'country' in request.GET:
            countries = request.GET['country']
            routes = routes.filter(country=countries)

        if 'route_type' in request.GET:
            route_types = request.GET['route_type'].split(',')
            routes = routes.filter(route_type__name__in=route_types)
            route_types = RouteType.objects.filter(name__in=route_types)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('routes'))

            queries = Q(name__icontains=query) | (
                Q(description__icontains=query) |
                Q(country__icontains=query) |
                Q(length__icontains=query) |
                Q(route_type__friendly_name__icontains=query) |
                Q(bike_type__friendly_name__icontains=query))
            routes = routes.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'routes': routes,
        'search_term': query,
        'current_biketypes': biketypes,
        'current_countries': countries,
        'current_route_types': route_types,
        'current_sorting': current_sorting,
    }
    return render(request, 'routes/routes.html', context)


def route_detail(request, route_id):
    """ A view to show individual route details """
    route = get_object_or_404(Route, pk=route_id)
    is_saved = False
    if route.save_route.filter(id=request.user.id).exists():
        is_saved = True

    context = {
        'route': route,
        'not_basket': True,
        'is_saved': is_saved,
    }
    return render(request, 'routes/route_detail.html', context)


@login_required
def add_route(request):
    """ Add a route to the site """
    if request.method == 'POST':
        form = RouteForm(request.POST, request.FILES)
        user = request.user
        if form.is_valid():
            route = form.save(commit=False)
            route.user = user
            route.save()
            messages.success(request, 'Successfully added a new route!')
            return redirect(reverse('route_detail', args=[route.id]))
        else:
            messages.error(request, 'Failed to add new route. \
                Please ensure the form is valid.')
    else:
        form = RouteForm()
    template = 'routes/add_route.html'
    context = {
        'form': form,
        'not_basket': True
    }
    return render(request, template, context)


@login_required
def edit_route(request, route_id):
    """ Edit an existing route """
    route = get_object_or_404(Route, pk=route_id)
    if request.method == 'POST':
        form = RouteForm(request.POST, request.FILES, instance=route,)
        if form.is_valid():
            form.save()
            messages.success(request,
                             f'You have successfully updated {route.name}')
            return redirect(reverse('route_detail', args=[route.id]))
        else:
            messages.error(
                request, 'Failed to update route. \
                    Please ensure the form is valid.')
    else:
        # Only users who added the route can edit the route
        if request.user == route.user:
            form = RouteForm(instance=route)
            messages.info(request, f'You are now editing {route.name}')

            template = (
                'routes/edit_route.html')
            context = {
                'form': form,
                'route': route,
            }
            return render(request, template, context)
        else:
            messages.warning(
                request, f'Sorry, you do not have \
                    authorization to edit {route.name}. \
                        You can only edit routes you uploaded.')
            return redirect(reverse('route_detail', args=[route.id]))


@login_required
def delete_route(request, route_id):
    """ Delete a route from the database """
    route = get_object_or_404(Route, pk=route_id)
    # Only users who added the route can delete the route
    if request.user == route.user:
        route = get_object_or_404(Route, pk=route_id)
        route.delete()
        messages.success(request, f'You have deleted {route.name}')
        return redirect(reverse('routes'))
    else:
        messages.warning(
            request, f'Sorry, you do not have \
                authorization to delete {route.name}. \
                    You can only delete routes you uploaded.')
        return redirect(reverse('route_detail', args=[route.id]))


def add_instructions(request):
    """ A view to render the add route instructions """
    template = 'routes/add_instructions.html'
    return render(request, template)


@login_required
def save_route_list(request):
    """ A view to render the users saved routes """
    user = request.user
    saved_routes = user.save_route.all()

    context = {
        'saved_routes': saved_routes,
    }
    return render(request, 'routes/saved_routes.html', context)


@login_required
def save_route(request, route_id):
    """ A view to check membership conditions \
        and get/save route if possible """
    route = get_object_or_404(Route, pk=route_id)
    profile = get_object_or_404(UserProfile, user=request.user)
    user = request.user
    saved_routes = user.save_route.all()

    if profile.membership and \
            profile.membership.name == 'unlimited_membership':
        if not route.save_route.filter(id=request.user.id).exists():
            route.save_route.add(request.user)
            messages.success(request, 'You have added\
                this route to your saved routes. See map below.')
            return redirect(reverse('route_detail', args=[route.id]))
        else:
            # Required in the event that the user types the url in manually
            messages.info(request, 'You already have \
                this route saved. See map below.')
            return redirect(reverse('route_detail', args=[route.id]))

    elif profile.membership and \
            profile.membership.name == 'limited_membership':
        if saved_routes.count() < 5:
            if not route.save_route.filter(id=request.user.id).exists():
                route.save_route.add(request.user)
                messages.success(request, 'You have \
                    added this route to your saved routes. See map below.')
                return redirect(reverse('route_detail', args=[route.id]))
            else:
                # Required in the event that the user types the url in manually
                messages.info(request, 'You already have \
                    this route saved. See map below.')
                return redirect(reverse('route_detail', args=[route.id]))
        else:
            messages.warning(request, 'You have already \
                reached your membership limit this month. \
                    Please wait till next month or upgrade to Unlimited')
            return redirect(reverse('route_detail', args=[route.id]))

    elif profile.membership and \
            profile.membership.name == 'trial_membership':
        if saved_routes.count() < 1:
            if not route.save_route.filter(id=request.user.id).exists():
                route.save_route.add(request.user)
                messages.success(request, 'You have added \
                    this route to your saved routes. See map below.')
                return redirect(reverse('route_detail', args=[route.id]))
            else:
                # Required in the event that the user types the url in manually
                messages.info(request, 'You already have \
                    this route saved. See map below.')
                return redirect(reverse('route_detail', args=[route.id]))
        else:
            messages.warning(request, 'You have \
                already reached your membership limit this month.\
                     Please wait till next month or upgrade to Unlimited')
            return redirect(reverse('route_detail', args=[route.id]))

    else:
        messages.info(request, 'You currently have no Membership. \
            Check out the membership options on this page')
        return redirect(reverse('membership'))
