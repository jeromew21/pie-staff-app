from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as authViews
from .views import domainErrorView, publicSnippetView, \
    home, SnippetEditView, SnippetCreateView, SnippetsView, logoutView, CreateIssueView, \
    IssuesView

urlpatterns = [
    url(r'^login/$', authViews.LoginView.as_view(), name='login'),
    url(r'^logout/$', logoutView, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url(r'^domainError/', domainErrorView),
    path('snippet/<name>/', publicSnippetView),
    path('newSnippet/', SnippetCreateView.as_view()),
    path('snippet/<name>/edit/', SnippetEditView.as_view()),
    path('snippet/', SnippetsView.as_view()),
    path('snippets/', SnippetsView.as_view()),
    path('newIssue/', CreateIssueView.as_view()),
    path('issues/', IssuesView.as_view()),
    url(r'^$', home, name='home'),
]