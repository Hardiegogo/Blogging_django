from django.shortcuts import render,get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    stuff={'posts':posts}
    return render(request,'blog/post_list.html',stuff)

def detail(request,pk):
    post= get_object_or_404(Post, pk=pk)
    stuff={'post':post}
    return render(request,'blog/detail.html',stuff)

def new_post(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('detail',pk=post.pk)
    else :
        form=PostForm()
        stuff={'form':form}
        return render(request,'blog/new_post.html', stuff)


def edit_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            post1=form.save(commit=False)
            post1.author=request.user
            post1.save()
            return redirect('detail',pk=post.pk)

    else:
        form=PostForm(instance=post)
        stuff={'form':form}
        return render(request,'blog/new_post.html', stuff)

def post_draft_list(request):
    posts=Post.objects.filter(published_date=None)
    stuff={"posts":posts}
    return render(request,'blog/post_draft_list.html',stuff)

def post_publish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect("detail",pk=pk)
