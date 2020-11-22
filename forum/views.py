from django.shortcuts import render, reverse, redirect, get_object_or_404
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


def view_post(request, post_id):
    """ A view to render the selected post along with any comments """
    post = get_object_or_404(ForumPost, pk=post_id)
    post_replies = ForumPostReply.objects.filter(
        post_id=post_id).order_by('-reply_date')

    template = 'forum/view_post.html'
    context = {
        'post': post,
        'post_replies': post_replies,
    }
    return render(request, template, context)


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
