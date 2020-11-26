from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'subject',
            'message',
            'copy_myself',
        ]

    def __init__(self, *args, **kwargs):
        """ Setting paceholder names """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full Name',
            'email': 'Email Address',
            'subject': 'Subject',
            'message': 'Your message here...',
            'copy_myself': '',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            if field != 'copy_myself':
                self.fields[field].label = False
            else:
                self.fields[field].label = 'Send me a copy'
