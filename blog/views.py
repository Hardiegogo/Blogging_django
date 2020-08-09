from django.shortcuts import render,get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    stuff={'posts':posts}
    return render(request,'blog/post_list.html',stuff)

def detail(request,pk):
    post= get_object_or_404(Post, pk=pk)
    stuff={'post':post}
    return render(request,'blog/detail.html',stuff)
