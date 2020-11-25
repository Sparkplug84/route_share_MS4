from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings


def contact(request):
    """ A view to render the contact form """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            sender = form.cleaned_data['email']
            message = form.cleaned_data['message']
            recipients = [settings.EMAIL_HOST_USER]

            send_mail(
                'New Contact Message',
                'Hi Route Share Team, \n\nThere is a new '
                f'contact message from {name}.\n'
                f'Email address of the sender is {sender}\n'
                f'Sender left the following message: \n\n{message}\n\n'
                'This email was automatically generated.',
                sender,
                recipients,
                fail_silently=False)
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
        'not_basket': False
    }
    return render(request, template, context)
