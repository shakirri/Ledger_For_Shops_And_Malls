from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login1(request):
    return render(request, "login.html")

def checkpass(request):

    val_user= request.POST['username']
    val_pass= request.POST['password']
    return render(request, "home.html")