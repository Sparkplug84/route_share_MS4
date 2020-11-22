from django.shortcuts import render
from .models import ForumPost, ForumPostReply
from .forms import ForumForm


def forum(request):
    """ A view to return index page """
    forum_posts = ForumPost.objects.order_by('-post_date')

    context = {
        'forum_posts': forum_posts,
    }
    return render(request, 'forum/forum.html', context)


def add_post(request):
    """ A view to add a new post to the forum page """
    form = ForumForm()
    template = 'forum/add_post.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
