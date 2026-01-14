from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
#id (primary key auto-incremented)
#frist_name (string), last_name (string), email (string), phone (string), created_date (date), description (text), category (foreign key), show (boolean), owner (foreign key), picture (image)

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Contact(models.Model):
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=70, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20)
    
    created_date = models.DateTimeField(default=timezone.now)
    
    description = models.TextField(blank=True)
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    show = models.BooleanField(default=True)
    
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    picture = models.ImageField(upload_to='contact_pictures/%Y/%m/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
