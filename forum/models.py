from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class ForumPost(models.Model):
    """ A model with all data required to create post in the form """
    title = models.CharField(max_length=100)
    post = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    post_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ForumPostReply(models.Model):
    """ A model with associated fields to reply to forum post """
    reply = models.TextField()
    reply_date = models.DateTimeField(default=timezone.now)
    reply_user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE)

    def __str__(self):
        return self.reply
