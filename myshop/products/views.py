from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    user = "Alejo"
    products_numb = 4
    return render(request, "products/home.html", {
            "name": user,
            "product_numb": products_numb,
        })

def productCat(request, product):
    if product == "suits" or product == "dresses" or product == "shirts" or product == "shoes":
        return HttpResponse(f"Here is the list of our {product}")
    else:
        return HttpResponse("The page you are looking for doesn't exist")
    
def signup(request):
    return render(request, "products/signup.html")