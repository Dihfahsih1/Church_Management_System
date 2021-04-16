from django import forms

from com.models import Comment
from com.conf import settings
from com.messages import EmailInfo


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {'content': forms.Textarea(attrs={'rows': 1})}

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        if self.request.user.is_anonymous and settings.COMMENT_ALLOW_ANONYMOUS:
            self.fields['email'] = forms.EmailField(
                label=EmailInfo.LABEL,
                widget=forms.EmailInput(attrs={
                    'placeholder': EmailInfo.INPUT_PLACEHOLDER,
                    'title': EmailInfo.INPUT_TITLE
                    })
                )

    def clean_email(self):
        """this will only be executed when email field is present for unauthenticated users"""
        email = self.cleaned_data['email']
        return email.strip().lower()
