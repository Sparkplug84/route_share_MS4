from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """ A view to render the contact form """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have sent a message to the Route Share Team. \
                             We will reply as soon as possible.')
        else:
            messages.error(request, 'Failed to send message. \
                Please ensure the form is valid.')

    form = ContactForm()
    template = 'contact/contact.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
