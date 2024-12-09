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

class makananrestoran(models.Model):
    NamaMakanan = models.CharField(max_length=100)
    HargaMakanan = models.DecimalField(max_digits=10, decimal_places=2)

class restoran(models.Model):
    namarestoran = models.CharField(max_length=100)
    alamatrestoran = models.CharField(max_length=200)

    def _str_(self):
        return self.name