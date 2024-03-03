from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('products/<product>', views.productCat, name="productcat"), 
    path('signup', views.signup, name="signup"),
    path('products/<productBrand>/<productSlug>', views.productPage, name="productPage")
]
