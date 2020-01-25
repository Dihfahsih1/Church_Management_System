from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .forms import RegisterForm
from dashboard.models import User
from django.contrib.auth.decorators import login_required

# def loginpage(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password =  request.POST['password']
#         post = User.objects.filter(username=username)
#         if post:
#             username = request.POST['username']
#             request.session['username'] = username
#             messages.success(request, f'Welcome..,You have successfully logged in')
#             return redirect("index")
#         else:
#             return render(request, 'users/home/login.html', {})
#     return render(request, 'users/home/login.html', {})
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
