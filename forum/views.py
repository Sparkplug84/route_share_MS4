from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ForumPost, ForumPostReply
from .forms import ForumForm, ForumReplyForm


def forum(request):
    """ A view to return index page """
    forum_posts = ForumPost.objects.order_by('-post_date')
    post_replies = ForumPostReply.objects.all()

    context = {
        'forum_posts': forum_posts,
        'post_replies': post_replies,
        'on_forum_page': True
    }
    return render(request, 'forum/forum.html', context)


def view_post(request, post_id):
    """ A view to render the selected post along with any comments """
    post = get_object_or_404(ForumPost, pk=post_id)
    post_replies = ForumPostReply.objects.filter(
        post_id=post_id).order_by('-reply_date')

    if request.method == 'POST':
        form = ForumPostReply(
            reply=request.POST.get('reply'),
            reply_user=request.user,
            post=post,
        )
        form.save()
        messages.success(request, 'You have replied to this post!')
        return redirect('view_post', post_id)

    else:
        form = ForumReplyForm()
    template = 'forum/view_post.html'
    context = {
        'form': form,
        'post': post,
        'post_replies': post_replies,
        'on_forum_page': True
    }
    return render(request, template, context)


@login_required
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


@login_required
def edit_post(request, post_id):
    """ A view to edit a forum post """
    post = get_object_or_404(ForumPost, pk=post_id)
    if request.method == 'POST':
        form = ForumForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, f'You have updated {post.title}')
            return redirect('view_post', post_id)
        else:
            messages.error(request, 'Failed to update post. \
                    Please ensure the form is valid.')
            return redirect('view_post', post_id)
    else:
        if request.user == post.post_user:
            form = ForumForm(instance=post)
            messages.info(request, f'You are now editing {post.title}')

            template = 'forum/edit_post.html'
            context = {
                'form': form,
                'post': post,
            }
            return render(request, template, context)
        else:
            messages.warning(request, f'Sorry, you do not have \
                    authorization to edit {post.title}. \
                        You can only edit posts you uploaded.')
        return redirect('view_post', post_id)


@login_required
def delete_post(request, post_id):
    """ A view to delete a post """
    post = get_object_or_404(ForumPost, pk=post_id)
    # Only users who added the post can delete the post
    if request.user == post.post_user:
        post.delete()
        messages.success(request, f'You have deleted {post.title}')
        return redirect('forum')
    else:
        messages.warning(
            request, f'Sorry, you do not have \
            authorization to delete {post.title}. \
                You can only delete posts you added.')
        return redirect('forum')
