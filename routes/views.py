from django.shortcuts import render
from .models import Route

# Create your views here.


def all_routes(request):
    """ A view to show all routes, including sorting and search queries """

    routes = Route.objects.all()

    context = {
        'routes': routes,
    }
    return render(request, 'routes/routes.html', context)
