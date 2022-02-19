from django.shortcuts import render, redirect
from .models import Movie, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

def movie_list(request):
	movies = Movie.objects.all()
	categories = Category.objects.all()
	context = {
		'movies': movies,
		'categories': categories
	}
	return render(request, 'profiles/movie_list.html', context)

@login_required(login_url='/login_page')
def my_profile(request):
	profile = request.user.profile
	context = {
		'profile': profile
	}
	return render(request, 'profiles/profile.html', context)


def login_page(request):
	""" Страница для входа """
	# для перекидывания аутентифицированного пользователя
	if request.user.is_authenticated:
		return redirect('my_profile')
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('my_profile')
	return render(request, 'profiles/login_page.html')

def logout_page(request):
	logout(request)
	return redirect('movie_list')


def category(request,id):
	category = get_object_or_404(Category, id=id)
	movies = category.movie_set.all()
	context = {
		'movies': movies
	}
	return render(request, 'profiles/category.html', context)

