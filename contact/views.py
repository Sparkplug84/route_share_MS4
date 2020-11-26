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
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipients = [settings.EMAIL_HOST_USER]
            copy_myself = form.cleaned_data['copy_myself']

            if copy_myself:
                recipients.append(sender)

            form.save()

            send_mail(
                f'New Contact Message - {subject}',
                'Hi Route Share Team, \n\nThere is a new '
                f'contact message from {name}.\n'
                f'Email address of the sender is {sender}\n'
                f'Sender left the following message: \n\n{message}\n\n'
                'This email was automatically generated.',
                sender,
                recipients,
                fail_silently=False)

            messages.success(request, 'You have sent a message to the Route Share Team. \
                             We will reply as soon as possible.')
        else:
            messages.error(request, 'Failed to send message. \
                Please ensure the form is valid.')

    form = ContactForm()
    template = 'contact/contact.html'
    context = {
        'form': form,
        'not_basket': True
    }
    return render(request, template, context)
