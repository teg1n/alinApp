from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Share(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    content = models.TextField()   
    foto = models.ImageField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"
    

# models.py
from django.db import models
from django.contrib.auth.models import User

class Sharing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=150)
    foto = models.ImageField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)