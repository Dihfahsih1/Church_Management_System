from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account has been created successfully!, you can now login')
			return redirect('login')
	else:
		form = RegisterForm()
	return render(request, 'users/home/register.html', {'form': form})

