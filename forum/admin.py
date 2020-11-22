from django.contrib import admin
from .models import ForumPost, ForumPostReply


# Registered Models for Admin
admin.site.register(ForumPost)
admin.site.register(ForumPostReply)
