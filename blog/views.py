from django.shortcuts import render,get_object_or_404, redirect
from .models import Post,Comment
from django.utils import timezone
from .forms import PostForm,CommentForm,UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.
def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    stuff={'posts':posts}
    return render(request,'blog/post_list.html',stuff)

def detail(request,pk):
    post= get_object_or_404(Post, pk=pk)
    stuff={'post':post}
    return render(request,'blog/detail.html',stuff)

@login_required
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

@login_required
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

@login_required
def post_draft_list(request):
    posts=Post.objects.filter(published_date=None)
    stuff={"posts":posts}
    return render(request,'blog/post_draft_list.html',stuff)

@login_required
def post_publish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect("detail",pk=pk)

@login_required
def post_delete(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect('post_list')


def add_comment(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid:
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('detail',pk=post.pk)
    else:
        form=CommentForm()
        return render(request,"blog/add_comment.html",{'form':form})


@login_required
def comment_approve(request, pk):

    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):

    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('detail', pk=comment.post.pk)

def signup(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            new_user=User.objects.create_user(**form.cleaned_data)
            login(request,new_user)
            return redirect('/')

    else:
        form=UserForm()
        return render(request,'registration/signup.html',{'form':form})
