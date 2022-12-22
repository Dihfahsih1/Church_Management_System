from django.conf.urls import url
from django.urls import reverse,path
from . import views

urlpatterns=[
    path('', views.website, name="website"),
]