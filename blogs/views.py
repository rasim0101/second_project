from django.shortcuts import render
from .models import Blog, Comment

def blog_list(request):
	blogs = Blog.objects.all().prefetch_related('comment_set')
	context = {
		'blogs': blogs
	}
	return render(request, 'blogs/blog_list.html', context)

def comment_list(request):
	comments = Comment.objects.all().select_related('blog')
	context = {
		'comments': comments
	}
	return render(request, 'blogs/comment_list.html', context)

