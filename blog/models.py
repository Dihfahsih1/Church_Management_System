from django.db import models
from django.utils import timezone
from dashboard.models import *
from django.urls import reverse

class posts(models.Model):
    Title = models.CharField(max_length=100)
    Post_content = models.TextField()
    Date_posted = models.DateTimeField(default=timezone.now)#auto_now_add=True
    Name = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
