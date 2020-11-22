from django.shortcuts import render
from .models import ForumPost, ForumPostReply


def forum(request):
    """ A view to return index page """
    forum_posts = ForumPost.objects.all()

    context = {
        'forum_posts': forum_posts,
    }
    return render(request, 'forum/forum.html', context)
