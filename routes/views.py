from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Route, BikeType, RouteType

# Create your views here.


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
            # if sortkey == 'country':
            #     sortkey = 'country__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            routes = routes.order_by(sortkey)

        if 'bike_type' in request.GET:
            biketypes = request.GET['bike_type'].split(',')
            routes = routes.filter(bike_type__name__in=biketypes)
            biketypes = BikeType.objects.filter(name__in=biketypes)

        if 'country' in request.GET:
            countries = request.GET['country']
            routes = routes.filter(country=countries)
            # countries = Route.objects.filter(country=countries)

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

    context = {
        'route': route,
    }
    return render(request, 'routes/route_detail.html', context)
