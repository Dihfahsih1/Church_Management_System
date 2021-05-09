from django import forms
from dashboard.models import User
from dashboard.views import *

"""form for creating a system user from the dashboard"""
class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['full_name','username','Role','Is_View_on_Web']
        labels = {
            'full_name': 'Name',
            'email': 'Email',
            'username': 'Username',
        }
        error_messages = {
            'full_name': {
                'max_length': "Name can only be 25 characters in length"
            }
        }
        widgets = {
            'full_name': autocomplete.ModelSelect2(url='auto-complete',
            attrs={'data-placeholder': 'Type here the name....', 'data-minimum-input-length': 3})
        }
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
    
class MembershipAccountForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='Repeat Password',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password Confirmation'}))

    class Meta:
        model = User
        fields = ['avatar','fname', 'lname','email','username',]
        labels = {
            'avatar':'Profile Photo',
            'fname':'First Name',
            'lname':'Second Name',
            'email': 'Email',
            'username': 'Username',
            
        }
        
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(MembershipAccountForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['full_name','email','username','Role']

class UserLoginForm(forms.Form):
    username=forms.CharField(label='Username/Email')
    password=forms.CharField(label='Password',widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
        query=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        user_qs_final=User.objects.filter(
                Q(username__iexact=query)|
                Q(email__iexact=query)
            ).distinct()
        if not user_qs_final.exists() and user_qs_final!=1:
            raise forms.ValidationError("Invalid credentials-user does not exits")
        user_obj=user_qs_final.first()
        if not user_obj.check_password(password):
            raise forms.ValidationError("credential are wrong")
        self.cleaned_data["user_obj"]=user_obj
        return super(UserLoginForm,self).clean(*args,**kwargs)


