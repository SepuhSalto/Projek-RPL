from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=30, default = 'John')
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    Lokasi = models.CharField(max_length=100, default = 'Jakarta')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    