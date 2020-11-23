from django import forms
from .models import ForumPost, ForumPostReply


class ForumForm(forms.ModelForm):

    class Meta:
        model = ForumPost
        fields = [
            'title',
            'post',
        ]

    def __init__(self, *args, **kwargs):
        """ Setting paceholder names """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Post Title',
            'post': 'Your Post',
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False


class ForumReplyForm(forms.ModelForm):

    class Meta:
        model = ForumPostReply
        fields = [
            'reply',
        ]

    reply = forms.CharField(
        required=True,
        label='',
        widget=forms.Textarea(attrs={
            'rows': 2,
            'class': 'form-control',
            'placeholder': 'Add your reply...'
        })
    )
