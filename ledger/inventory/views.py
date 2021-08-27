from django.http import HttpResponse
from django.shortcuts import render
from .models import Products
from .tempo import Pricing, SalesTemp

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
    prod=Products.objects.all()
    return render(request, "productlist.html", {'prods':prod})

def home(request):
    return render(request, "home.html")

def sell(request):
    x=Pricing(id=1, total_price=0, profit=0)
    x.save()
    v=SalesTemp.objects.all()
    v.delete()
    return render(request, "sales.html")

def addsales(request):
    pid= request.POST['product_id']
    pamount= int(request.POST['amount'])
    x=Products.objects.get(id=pid)
    p=Pricing.objects.get(id=1)
    s=SalesTemp(id=pid, name=x.name, amount=pamount, purchase_price=x.purchase_price, sale_price=x.sale_price)
    #if p.total_price==None:
    #    p.total_price=0
    #tp=p.total_price
    s.per_total=x.sale_price*pamount
    p.total_price=p.total_price+x.sale_price*pamount
    #p.profit=0
    s.save()
    p.save()
    priceT= Pricing.objects.all()

    saleslist=SalesTemp.objects.all()
    context = {
        'list':saleslist,
        'price':priceT
 
    }
    #for pr in SalesTemp.objects.all():

       # saleslist=saleslist+pr
    #saleslist=[p]
    return render(request, "sales.html", context)

def sold(request):
    for sl in SalesTemp.objects.all():
        x=Products.objects.get(id=sl.id)
        x.amount=x.amount-sl.amount
        x.save()
    return render(request, "home.html")

def balance(request):
    return render(request, "ledger.html")