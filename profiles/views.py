from django.shortcuts import render


def profile(request):
    """ View to render the user profile """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)