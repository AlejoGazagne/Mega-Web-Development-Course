from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank = True)
    
    def __str__(self):
        return f"{self.title}"

class Address(models.Model):
    street = models.CharField(max_length = 100)
    zipcode = models.PositiveIntegerField()
    city = models.CharField(max_length = 20)
    country = models.CharField(max_length = 20)
    
    def __str__(self):
        return f"{self.country} - {self.city}"

class Brand(models.Model):
    title = models.CharField(max_length = 70)
    logo = models.ImageField()
    addres = models.OneToOneField(Address, on_delete = models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.title}"
    
class Shirt(models.Model):
    title = models.CharField(max_length = 70)
    price = models.PositiveIntegerField()
    brand = models.ForeignKey(Brand, null=True, on_delete = models.CASCADE)
    description = models.TextField(blank = True)
    is_bestseller = models.BooleanField(default = False)
    
    def __str__(self):
        return f"{self.title}"
    
class Product(models.Model):
    title = models.CharField(max_length = 70)
    description = models.TextField(blank = True)
    category = models.ManyToManyField(Category)
    image = models.ImageField(blank = True, upload_to='product-img')
    brand = models.ForeignKey(Brand, on_delete= models.CASCADE, null=True, related_name="product")
    price = models.PositiveIntegerField()
    slug = models.SlugField(blank=True)
    is_bestseller = models.BooleanField(default = False)
    suggestions = models.ManyToManyField('self')
    
    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = self.id
        super().save(*args, **kwargs)