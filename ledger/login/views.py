from django.http import HttpResponse
from django.shortcuts import render
from .models import Users

# Create your views here.
def login1(request):
    return render(request, "login.html")

def checkpass(request):
    val_user= request.POST['username']
    val_pass= request.POST['password']
    x=Users.objects.filter(userid=val_user)
    if len(x)==0:
        return render(request, "error.html");
    a=Users.objects.get(userid=val_user)
    if(a.passw==val_pass):
        return render(request, "home.html");
    else:
        return render(request, "error.html");