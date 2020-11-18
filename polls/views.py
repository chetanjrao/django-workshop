from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import Tweet

@login_required
def tweets(request):
    tweets = Tweet.objects.all()
    return render(request, "index.html", { "tweets": tweets })

def tw_login(request):
    if request.method == "POST":
        username = request.POST["uname"]
        password = request.POST["pwd"]
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, "login.html", { "error": "username or password is wrong" })
        else:
            login(request, user)
            return redirect('home')
    return render(request, "login.html")