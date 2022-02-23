from django.shortcuts import render
from .models import Blog, Comment

def blog_list(request):
	blogs = Blog.objects.all()
	context = {
		'blogs': blogs
	}
	return render(request, 'blogs/blog_list.html', context)

def comment_list(request):
	comments = Comment.objects.all()
	context = {
		'comments': comments
	}
	return render(request, 'blogs/comment_list.html', context)

