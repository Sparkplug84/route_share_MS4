from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages


@login_required
def profile(request):
    """ View to render the user profile """
    profile = get_object_or_404(UserProfile, user=request.user)
    user = request.user
    saved_routes = user.save_route.all()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid:
            form.save()
            messages.success(request, 'Profile succesfully updated')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': profile,
        'not_basket': True,
        'saved_routes': saved_routes,
    }
    return render(request, template, context)
