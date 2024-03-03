from django.contrib import admin
from .models import Shirt, Product, Brand

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    list_display = ("title", "id", "category", "price", "is_bestseller", "brand")
    list_filter = ("is_bestseller", )
    search_fields = ("title", "category", "brand")

# Register your models here.
admin.site.register(Shirt)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)