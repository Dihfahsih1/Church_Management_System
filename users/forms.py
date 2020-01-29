from django import forms
from dashboard.models import User

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['full_name','email','username','Role']
        # 'roles'

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

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['full_name','email','username','Role']

   
'''class UserEmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not email:
            return email
        try:
            user = User.objects.get(email=email)
            if user.email == self.instance.email:
                return email
        except User.DoesNotExist:
            return email

        raise ValidationError(_("This email is already used."))'''

