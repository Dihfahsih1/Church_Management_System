from django.db import models
from dashboard.models import User
from django.urls import reverse

class UserProfile(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True )

    # this method must be defined for appropriate url mapping in comments section
    def get_absolute_url(self):
        return reverse('member_profile')