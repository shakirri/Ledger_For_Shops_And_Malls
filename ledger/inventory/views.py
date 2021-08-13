from django.http import HttpResponse
from django.shortcuts import render
from .models import Products

# Create your views here.
def addprod(request):
    return render(request, "productexist.html")

def newprod(request):
    return render(request, "addproduct.html")

def oldprod(request):
    return render(request, "oldproduct.html")
    
def purchased(request):
    pid= request.POST['product_id']
    pname= request.POST['name']
    pamount= request.POST['amount']
    ppurchase_price= request.POST['purchase_price']
    psales_price= request.POST['sale_price']
    p=Products(id=pid, name=pname, amount=pamount, purchase_price=ppurchase_price, sales_price=psales_price)
    p.save()
    return render(request, "home.html")

def oldpurchased(request):
    pid= request.POST['product_id']
    pamount= request.POST['amount']
    return render(request, "home.html")      