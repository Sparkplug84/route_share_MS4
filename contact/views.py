from django.shortcuts import render
from .forms import ContactForm


def contact(request):  
    """ A view to render the contact form """
    form = ContactForm()
    template = 'contact/contact.html'
    context = {
        'form': form,
    }
    return render(request, template, context)

