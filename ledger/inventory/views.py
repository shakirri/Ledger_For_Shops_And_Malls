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
    p=Products(id=pid, name=pname, amount=pamount, purchase_price=ppurchase_price, sale_price=psales_price)
    p.save()
    return render(request, "home.html")

def oldpurchased(request):
    pid= request.POST['product_id']
    pamount= int(request.POST['amount'])
    x=Products.objects.get(id=pid)
    x.amount=x.amount+pamount
    x.save()
    return render(request, "home.html") 

def check_inv(request):
    prod1=Products.objects.get(id=202011)
    prod2=Products.objects.get(id=202108)
    prod=Products.objects.all()
    return render(request, "productlist.html", {'prods':prod})