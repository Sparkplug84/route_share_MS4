from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    subject = models.CharField(max_length=100)
    copy_myself = models.BooleanField(blank=True)
    contact_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.subject
