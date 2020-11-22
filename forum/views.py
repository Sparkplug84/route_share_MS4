from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .models import ForumPost, ForumPostReply
from .forms import ForumForm


def forum(request):
    """ A view to return index page """
    forum_posts = ForumPost.objects.order_by('-post_date')

    context = {
        'forum_posts': forum_posts,
        'on_forum_page': True
    }
    return render(request, 'forum/forum.html', context)


def add_post(request):
    """ A view to add a new post to the forum page """
    if request.method == 'POST':
        form = ForumForm(request.POST)
        user = request.user
        if form.is_valid():
            post = form.save(commit=False)
            post.post_user = user
            post.save()
            messages.success(request, 'You have added a new forum post!')
            return redirect(reverse('forum'))
        else:
            messages.error(request, 'Failed to add new post. \
                Please ensure the form is valid.')
    else:
        form = ForumForm()
    template = 'forum/add_post.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
