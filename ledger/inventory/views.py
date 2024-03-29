import inventory
from django.http import HttpResponse
from django.shortcuts import render
from .models import Products, Assets
from .tempo import Pricing, SalesTemp

# Create your views here.
def addprod(request):
    if not (Assets.objects.filter(id=1)):
        a=Assets.objects.create(id=1, cash=100000, profit=0, total_purchases=0, total_sales=0, inventory_value=0)
        a.save()

    return render(request, "productexist.html")

def newprod(request):
    return render(request, "addproduct.html")

def oldprod(request):
    return render(request, "oldproduct.html")
    
def purchased(request):
    a=Assets.objects.get(id=1)
    pid= request.POST['product_id']
    pname= request.POST['name']
    pamount= int(request.POST['amount'])
    ppurchase_price= int(request.POST['purchase_price'])
    psales_price= int(request.POST['sale_price'])
    p=Products(id=pid, name=pname, amount=pamount, purchase_price=ppurchase_price, sale_price=psales_price)
    p.save()
    cash=p.amount*p.purchase_price
    a.cash=a.cash-cash
    a.total_purchases=cash+a.total_purchases
    a.save()
    return render(request, "home.html")

def oldpurchased(request):
    a=Assets.objects.get(id=1)
    pid= request.POST['product_id']
    pamount= int(request.POST['amount'])
    x=Products.objects.get(id=pid)
    x.amount=x.amount+pamount
    x.save()
    cash=pamount*x.purchase_price
    a.cash=a.cash-cash
    a.total_purchases=cash+a.total_purchases
    a.save()
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
    p.profit=p.profit+pamount*(x.sale_price-x.purchase_price)
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
    a=Assets.objects.get(id=1)
    p=Pricing.objects.get(id=1)
    for sl in SalesTemp.objects.all():
        x=Products.objects.get(id=sl.id)
        x.amount=x.amount-sl.amount
        x.save()
    a.cash=a.cash+p.total_price
    a.profit=a.profit+p.profit
    a.total_sales=a.total_sales+p.total_price
    a.save()
    Pricing.objects.all().delete
    return render(request, "home.html")

def balance(request):
    a=Assets.objects.get(id=1)
    a.inventory_value=inventory_calc()
    asset=[a]
    context = {
        'list':asset,
 
    }
    return render(request, "ledger.html", context)

def inventory_calc():
    x=0
    for p in Products.objects.all():
        x=x+(p.purchase_price*p.amount)


    return x