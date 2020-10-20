from django.shortcuts import render
from .models import Membership

# Create your views here.


def membership(request):
    """ A view to return the membership page """
    memberships = Membership.objects.all()

    context = {
        'memberships': memberships,
    }
    return render(request, 'membership/membership.html', context)
