from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import PostForm
from blog.models import Post


def home(request):
    post = Post.objects.all()
    return render(request, 'home.html', {'posts': post})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def detail_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('home')






