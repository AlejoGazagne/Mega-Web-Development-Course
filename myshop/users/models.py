from django.db import models

# Create your models here.
class Profile(models.Model):
    fullName = models.CharField(max_length = 50)
    email = models.EmailField()
    birthDate = models.DateField()