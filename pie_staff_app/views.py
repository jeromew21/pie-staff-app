from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        return redirect('/login/')

def domainErrorView(request):
    return render(request, "generic.html", {"content": "Error logging in: Please use a pioneers.berkeley.edu email."})
