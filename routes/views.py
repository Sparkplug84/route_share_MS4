from django.shortcuts import render, get_object_or_404
from .models import Route

# Create your views here.


def all_routes(request):
    """ A view to show all routes, including sorting and search queries """

    routes = Route.objects.all()

    context = {
        'routes': routes,
    }
    return render(request, 'routes/routes.html', context)


def route_detail(request, route_id):
    """ A view to show individual route details """

    route = get_object_or_404(Route, pk=route_id)

    context = {
        'route': route,
    }
    return render(request, 'routes/route_detail.html', context)
