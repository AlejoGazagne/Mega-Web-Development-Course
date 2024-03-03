from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all().order_by('id')[:4]
    return render(request, "products/home.html",{
        "products": products,
    })

def productCat(request, product):
    if product == "suits" or product == "dresses" or product == "shirts" or product == "shoes":
        return HttpResponse(f"Here is the list of our {product}")
    else:
        return HttpResponse("The page you are looking for doesn't exist")
    
def signup(request):
    return render(request, "products/signup.html")

def productPage(request, productBrand, productSlug):
    product = Product.objects.get(slug=productSlug)
    if request.method == "GET":
        return render(request, "products/product.html", {
            "product": product
        })
    else:
        result = request.POST["username"]
        return render(request, "products/product.html", {
            "product": product,
            "result": result
        })