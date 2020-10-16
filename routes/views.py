from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Route, BikeType

# Create your views here.


def all_routes(request):
    """ A view to show all routes, including sorting and search queries """

    routes = Route.objects.all()
    query = None
    biketypes = None
    countries = None
    route_types = None

    if request.GET:

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

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error("You didn't enter any search criteria")
                return redirect(reverse('routes'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(country__icontains=query) | Q(route_type__icontains=query) | Q(length__icontains=query) 
            routes = routes.filter(queries)

    context = {
        'routes': routes,
        'search_term': query,
        'current_biketypes': biketypes,
        'current_countries': countries,
        'current_route_types': route_types,
    }
    return render(request, 'routes/routes.html', context)


def route_detail(request, route_id):
    """ A view to show individual route details """

    route = get_object_or_404(Route, pk=route_id)

    context = {
        'route': route,
    }
    return render(request, 'routes/route_detail.html', context)
