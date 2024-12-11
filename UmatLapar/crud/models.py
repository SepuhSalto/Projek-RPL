from django.db import models
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Users(models.Model):
    idpengguna = models.BigAutoField(primary_key=True, default=1)
    username = models.CharField(max_length=50, default='John Doe')
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    poin = models.IntegerField(default =0)
    hobi = models.TextField(blank=True)
    pekerjaan = models.TextField(max_length = 100, blank=True)
    alamat = models.TextField(blank=True)
    foto_profil = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Rating(models.Model):
    idrating = models.BigAutoField(primary_key=True, default=1)
    idpengguna = models.ForeignKey(Users, on_delete=models.CASCADE)
    idmenu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    rating = models.IntegerField()
    foto = models.ImageField(upload_to='images/', blank=True)
    video = models.FileField(upload_to='videos/', blank=True)
    komentar = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.idpengguna.username

class Restoran(models.Model):
    idrestoran = models.BigAutoField(primary_key=True, default=1)
    namaRestoran = models.CharField(max_length=50)
    waktuBuka = models.TimeField(blank=False)
    waktuTutup = models.TimeField(blank=False)
    alamat = models.TextField(blank=False)
    foto = models.ImageField(upload_to='images/', blank=True)
    hargaTerkecil = models.IntegerField()
    hargaTerbesar = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.namaRestoran

class Event(models.Model):
    idevent = models.BigAutoField(primary_key=True, default=1)
    idrestoran = models.ForeignKey(Restoran, on_delete=models.CASCADE)
    namaevent = models.CharField(max_length=50)
    deskripsi = models.TextField(blank=False)
    tanggal = models.DateField()
    lokasi = models.TextField(blank=False)
    foto = models.ImageField(upload_to='images/', blank=True)
    video = models.FileField(upload_to='videos/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.namaevent

class Menu(models.Model):
    idmenu = models.BigAutoField(primary_key=True, default=1)
    idrestoran = models.ForeignKey(Restoran, on_delete=models.CASCADE)
    namaMenu = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.namaMenu

@receiver(post_save, sender=Rating)
def add_points_on_rating(sender, instance, created, **kwargs):
    if created:
        user = instance.idpengguna
        user.poin += 10
        user.save()