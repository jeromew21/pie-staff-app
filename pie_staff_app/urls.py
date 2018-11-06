from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as authViews
from .views import *

urlpatterns = [
    url(r'^login/$', authViews.LoginView.as_view(), name='login'),
    url(r'^logout/$', authViews.LogoutView.as_view(), name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    path(r'domainError/', domainErrorView),
    url(r'^$', home, name='home'),
]