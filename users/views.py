from django.shortcuts import render, redirect
from .forms import NewUserForm
from profiles.forms import ProfileForm
from django.contrib.auth import login 
from django.contrib import messages
from profiles import views

def users_request(request):
	if request.method == 'POST':
		reg_form = NewUserForm(request.POST)
		if reg_form.is_valid():
			user = reg_form.save()
			login(request, user)
			messages.success(request, 'Registration successful.')
			return redirect('movie_list')
		messages.error(request, 'Unsuccessful regisrtation. Invalid information.')
	reg_form = NewUserForm()
	profile_form = ProfileForm()
	context = {
		'reg_form': reg_form,
		'profile_form': profile_form
	}
	return render(request=request, template_name='users/users.html', context=context)