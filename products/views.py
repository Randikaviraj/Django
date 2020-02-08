from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Product
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    try:
        products=Product.objects.all()
        return render(request,'main.html',{'products':products})
    except:
        return HttpResponse("404 Error is here")
        
        
    

def create(request):
    if request.method=="POST":
        id=request.POST.get('ProductID')
        name=request.POST.get('ProductName')
        price=request.POST.get('ProductPrice')
        Product.objects.create(product_id=id,product_name=name,product_price=price)
        return HttpResponseRedirect('/products/')
    
    return render(request,'create.html')
    
        

    
    

def delete(request,id):
    try:
        instance = get_object_or_404(Product,product_id=id)
        instance.delete()
    except:
        return HttpResponse("404 Error is here")
    
    return HttpResponseRedirect('/products/')
    

def search(request):
    name=request.GET.get('ProductName')
    print(type(name))
    print("...."+name)
    try:
        instance=Product.objects.get(product_name=name)
        return render(request,'instance.html',{"instance":instance,"message":"There is a Product called ","name":name})
    except:
        return render(request,'search.html',{"message":"There is no  Product called ","name":name})
    
    
def confirm(request):
    return HttpResponseRedirect('/products/')
        
    
    
    