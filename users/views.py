from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .forms import *
from django.http import HttpResponseForbidden
from dashboard.forms import *
from dashboard.models import *
from python_utils import *
from dashboard.views import *
from django.contrib.auth.views import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.contrib.auth import login, logout
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import user_passes_test

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
@login_required
def view_profile(request):
    context={}
    try:
        member_id=request.user.full_name.id
    except:
        member_id=request.user.id
        
    pledges=Pledges.objects.filter(Pledge_Made_By_id=member_id)
    tithes=Revenues.objects.filter(Revenue_filter='tithes',Member_Id=member_id)
    thanks=Revenues.objects.filter(Revenue_filter='thanks',Member_Id=member_id)
    context['thanks']=thanks
    context['pledges']=pledges
    context['tithes']=tithes
    context['member_id']=member_id
    return render(request, 'users/home/profile.html',context)

@login_required
def edit_profile(request):
    try:
        get_member = Members.objects.get(id=request.user.full_name.id)
    except:
        get_member = Members.objects.get(id=request.user.id)
        
    if request.method == 'POST':
        form = MembersForm(request.POST or None, request.FILES or None, instance=get_member)
        if form.is_valid():
            form.save()
            messages.success(request, f'Profile updated successfully.')
            return redirect('profile')
        else:
            form = MembersForm(instance=get_member)
            args = {'form': form}
            return render(request, 'users/home/update_profile.html', args)

    else:
        form = MembersForm(instance=get_member)
        args = {'form': form}
        return render(request, 'users/home/update_profile.html', args) 

#create an account for user from the dashboard
@login_required
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created successfully!, User can now Login')
            return redirect('register')
    else:
        form=RegisterForm()
        users = User.objects.filter(full_name__is_active=True)
        count_users = users.count()
        context={ 'form':form, 'users':users, 'count_users':count_users}
        return render(request, 'users/home/register.html', context)


@user_passes_test(lambda u: u.is_anonymous)
def MemberAccountRegister(request):
    members=Members.objects.all()
    if request.method == 'POST':
        form = MembershipAccountForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            member = Members.objects.create(username=user.username, created_by=user,First_Name=user.fname, Second_Name=user.lname, Email=user.email, Photo=avatar)
            messages.success(request, f'Account has been created successfully!, Please Complete the registration')
            current_site = get_current_site(request)  
            mail_subject = user.fname + " " + user.lname + ' Created Account'  
            mail_message ="This account needs approval from the Admin"  
            to_email = 'dihfahsihm@gmail.com' 
            from_email = user.email
            
            if mail_subject and mail_message and from_email:
                try:
                    send_mail(mail_subject, mail_message, from_email, [to_email])
                except BadHeaderError:
                    return HttpResponse('Make sure you enter correct info.')
            return redirect('member_profile')
    else:
        form = MembershipAccountForm()
    return render(request, 'users/home/membershipaccount.html', {'form': form,'members':members})
    
@login_required    
def member_profile(request):
    current_user = request.user.username
    members_created_by_a_user = Members.objects.filter(username=request.user)
    try:
        member = Members.objects.get(created_by=request.user)
        context={'members':members_created_by_a_user,'member':member, 'current_user':current_user}
    except:
        member = Members.objects.get(Full_Named=request.user.full_name)
        context={'members':members_created_by_a_user, 'member':member, 'current_user':current_user}
    return render(request,'home/profile.html',context)

def delete_user(request,pk):
    user= get_object_or_404(User, id=pk)
    user.delete()
    messages.success(request, "The User successfully deleted!")
    return redirect("register")
    
    
@login_required
def update_system_user(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form = form.save()
            messages.success(request, "The User info successfully updated!")
            return redirect('register')
        else:
            form = RegisterForm(instance=user)
            args = {'form': form,}
            return render(request, 'users/home/user_update.html', args)
    else:
        form = RegisterForm(instance=user)
        args = {'form': form,}
        return render(request, 'users/home/user_update.html', args)


@login_required
def church_user_account(request, user_pk):
    user = get_object_or_404(Members, created_by=user_pk)
    if request.method == "POST":
        form = MembersForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form = form.save()
            messages.success(request, "Your details were updated!")
            return redirect('member_profile')
        else:
            form = MembersForm(instance=user)
            args = {'form': form,}
            return render(request, 'Members/update_member_profile.html', args)
    else:
        form = MembersForm(instance=user)
        args = {'form': form,}
        return render(request, 'Members/update_member_profile.html', args)
        
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("index_public")