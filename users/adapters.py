from allauth.account.adapter import DefaultAccountAdapter

class AccountsAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=False):
        data = form.cleaned_data
        user.email = data['email']
        user.first_name = data['fname']
        user.last_name = data['lname']
        user.picture = data['avatar']
        user.id = data['username']
        if 'password1' in data:
            user.set_password(data['password1'])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        user.save()
        return user