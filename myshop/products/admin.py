from django.contrib import admin
from .models import Product, Brand, Address, Category

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    list_display = ("title", "id", "price", "is_bestseller", "brand")
    list_filter = ("is_bestseller", )
    search_fields = ("title", "category", "brand")

# Register your models here.
admin.site.register(Brand)
admin.site.register(Address)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)