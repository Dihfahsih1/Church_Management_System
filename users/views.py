from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .forms import *
from dashboard.forms import UserForm
from dashboard.models import User
from python_utils import *
from django.contrib.auth.views import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from blog.models import posts
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger



class UserPasswordChangeView(LoginRequiredMixin, View):
    form_class = PasswordChangeForm
    template_name = 'users/home/change_password.html'

    def get(self, request):
        return render(request, self.template_name, {
            'form': self.form_class(request.user)
        })

    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, f'Password updated successfully.')
        return render(request, self.template_name, {'form': form})

def reset_user_password(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)

    if not request.user.is_authenticated:
        return HttpResponseForbidden()

    password = password_generator()
    user.set_password(password)
    user.save()
    messages.success(request, "This user's password has been reset. Please notify the user of their new password.!")
    context = {'mod_user': user,
               'password': password}
    return render(request, 'users/home/reset_user_password.html', context)
def view_profile(request):
    return render(request, 'users/home/profile.html')

def edit_profile(request):
    if request.method == 'POST':
        form = UserForm(request.POST or None, request.FILES or None, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, f'Profile updated successfully.')
            return redirect('profile')

        else:
            form = UserForm(instance=request.user)
            args = {'form': form}
            return render(request, 'users/home/update_profile.html', args)

    else:
        form = UserForm(instance=request.user)
        args = {'form': form}
        return render(request, 'users/home/update_profile.html', args)            
@login_required
def register(request):
	users=User.objects.all()
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account has been created successfully!, User can now login')
			return redirect('register')
	else:
		form = RegisterForm()
	return render(request, 'users/home/register.html', {'form': form,'users':users})

def delete_user(request,pk):
    user= get_object_or_404(User, id=pk)
    if request.method == "GET":
        user.delete()
        messages.success(request, "The User successfully deleted!")
        return redirect("register")
    context= {'user': user}
    return render(request, 'users/home/delete_user.html', context)

def user_update(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form = form.save()
            return redirect('register')
        else:
            form = RegisterForm(instance=user)
            args = {'form': form,}
            return render(request, 'users/home/user_update.html', args)
    else:
        form = RegisterForm(instance=user)
        args = {'form': form,}
        return render(request, 'users/home/user_update.html', args)
