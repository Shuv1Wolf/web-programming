from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)

@login_required
def new_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:index')
    else:
        form = BlogPostForm()
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if post.owner != request.user:
        return redirect('blogs:index')

    if request.method == 'POST':
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    else:
        form = BlogPostForm(instance=post)
    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)
