from django import forms
from dashboard.models import User
from dashboard.views import *

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
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['full_name','username','Is_View_on_Web']
        labels = {
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

   


