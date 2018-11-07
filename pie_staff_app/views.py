from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Snippet, Issue
from .forms import SnippetForm, IssueForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

def logoutView(request):
    logout(request)
    return redirect("/")

def home(request):
    if request.user.is_authenticated:
        return render(request, "home.html", dict(content=renderIssues()))
    else:
        return redirect('/login/')

def publicSnippetView(request, name):
    snip = Snippet.objects.filter(name=name)
    if snip:
        return HttpResponse(snip[0].content)
    return render(request, "generic.html", {"content": f"{name} not found"})

def domainErrorView(request):
    return render(request, "generic.html", {"content": "Error logging in: Please use a pioneers.berkeley.edu email."})

def renderIssues():
    content = "<h1>Issues</h1>"
    content += ' '.join(f"<div><a href='/snippet/{issue.name}/edit/'>{issue.name}</a></div>" for issue in Issue.objects.all())
    return content
    
class IssuesView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "generic.html", dict(content=renderIssues()))

class CreateIssueView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "form.html", dict(form=IssueForm(), title="Create Issue"))
        
    def post(self, request):
        form = IssueForm(request.POST)
        if form.is_valid():
            iss = form.instance
            iss.author = request.user
            iss.save()
            return redirect("/issues/")
        return render(request, "form.html", dict(
            form=IssueForm(), 
            title="Create Issue",
            errors=form.errors
        ))

class SnippetsView(LoginRequiredMixin, View):
    def get(self, request):
        content = "<h1>Snippets</h1>"
        content += ' '.join(f"<div><a href='/snippet/{snip.name}/edit/'>{snip.name}</a></div>" for snip in Snippet.objects.all())
        return render(request, "generic.html", dict(content=content))

class SnippetCreateView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "form.html", dict(
            form=SnippetForm(), 
            title="Create a new snippet",
        ))

    def post(self, request):
        form = SnippetForm(request.POST)
        if form.is_valid():
            snip = form.instance
            snip.author = request.user
            snip.save()
            return redirect("/snippets/")
        return render(request, "form.html", dict(
            form=SnippetForm(), 
            title="Create a new snippet",
            errors=form.errors
        ))

class SnippetEditView(LoginRequiredMixin, View):
    def get(self, request, name):
        snip = Snippet.objects.filter(name=name)
        if snip:
            snip = snip[0]
            form = SnippetForm(instance=snip)
            if snip.author:
                author = snip.author.username
            else:
                author = ""
            return render(request, "form.html", dict(
                form=form, 
                title=f"Edit snippet {name}",
                after=f"<p>Permalink: <a href='/snippet/{name}/'>/snippet/{name}/</a></p><p>Author: {author}</p>"
            ))
        return redirect("/snippets/")
