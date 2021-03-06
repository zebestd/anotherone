from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Il(models.Model):
    name = models.CharField(max_length=30)
 
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)
 
    def __str__(self):
        return self.name

class Ilce(models.Model):
    il = models.ForeignKey(Il, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Usta(models.Model):
    user =  models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    website = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    telefon = models.CharField(max_length=200, null=True)
    desc = models.TextField(max_length=1000, null=True)
    il = models.ForeignKey(Il, on_delete=models.SET_NULL, null=True)
    ilce = models.ForeignKey(Ilce, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(default='ananas.jpg',
                              upload_to='profile_images')

    def __str__(self):
        return self.name 

