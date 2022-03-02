from django.shortcuts import render, get_object_or_404
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

def comment_detail(request, id):
	comment = get_object_or_404(Comment, id=id)
	context = {
		'comment': comment
	}
	return render(request, 'blogs/comment_detail.html', context)

def blog_detail(request, slug):
	blog = get_object_or_404(Blog, slug=slug)
	context = {
		'blog': blog
	}
	return render(request, 'blogs/blog_detail.html', context)

