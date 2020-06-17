from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include,path,re_path
from django.contrib.auth.views import *
from django.views.generic import TemplateView
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [ 
    path('admin', admin.site.urls),
    path('', include('dashboard.urls')),
    re_path('^',include('django.contrib.auth.urls')),
    path('register/', user_views.register, name='register'),
    path('MemberAccountRegister/', user_views.MemberAccountRegister, name='MemberAccountRegister'),
    url(r'^profile/', user_views.view_profile, name='profile'),
    url(r'^update/profile/', user_views.edit_profile, name='edit-profile'),
    url(r'^System-Users/delete/(?P<pk>\d+)', user_views.delete_user, name='delete-user'),
    url(r'^password/change/', user_views.UserPasswordChangeView.as_view(), name='changing-password'),
    path('Login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('Logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    url(r'^Password-Reset/', auth_views.PasswordResetView.as_view(template_name='users/home/password_reset.html'),
        name='password_reset'),
    url(r'^Done/Password-Reset', auth_views.PasswordResetDoneView.as_view(template_name='users/home/password_reset_done.html'),
        name='password_reset_done'),
    url(r'^Complete/Password-Reset', auth_views.PasswordResetCompleteView.as_view(template_name='users/home/password_reset_complete.html'),
        name='password_reset_complete'),
    url(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.PasswordResetConfirmView.as_view(template_name='users/home/password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^administrator/user/update/(?P<user_pk>\d+)/$', user_views.user_update, name='user_update'),
    url(r'^Reseting-Password/(?P<user_pk>\d+)/password/reset/$', user_views.reset_user_password, name='reset_user_password'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)