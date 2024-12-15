from django.db import models
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg, Count, Q
from django.core.paginator import Paginator
from collections import defaultdict

# Create your models here.
class Users(models.Model):
    idpengguna = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50, default='John Doe')
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    poin = models.IntegerField(default=0)
    hobi = models.TextField(blank=True)
    pekerjaan = models.TextField(max_length=100, blank=True)
    alamat = models.TextField(blank=True)
    foto_profil = models.ImageField(upload_to='images/', blank=True, default='images/default.jpg')
    foto_background = models.ImageField(upload_to='images/', blank=True, default='images/default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Location(models.Model):
    idlocation = models.BigAutoField(primary_key=True)
    lokasi = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.lokasi

class Rating(models.Model):
    idrating = models.BigAutoField(primary_key=True)
    idpengguna = models.ForeignKey(Users, on_delete=models.CASCADE)
    idmenu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    rating = models.IntegerField()
    foto = models.ImageField(upload_to='images/', blank=True, default='default.jpg')
    video = models.FileField(upload_to='videos/', blank=True)
    komentar = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.idpengguna.username

class kategori(models.Model):
    idkategori = models.BigAutoField(primary_key=True)
    kategori = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.kategori
        
class Restoran(models.Model):
    idrestoran = models.BigAutoField(primary_key=True)
    idlocation = models.ForeignKey(Location, on_delete=models.CASCADE, default=1)
    namaRestoran = models.CharField(max_length=50)
    waktuBuka = models.TimeField(blank=False)
    waktuTutup = models.TimeField(blank=False)
    alamat = models.TextField(blank=False)
    foto = models.ImageField(upload_to='images/', blank=True, default='images/default.jpg')
    hargaTerkecil = models.IntegerField()
    hargaTerbesar = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.namaRestoran


class Menu(models.Model):
    idmenu = models.BigAutoField(primary_key=True)
    idkategori = models.ForeignKey(kategori, on_delete=models.CASCADE, default=1)
    idrestoran = models.ForeignKey(Restoran, on_delete=models.CASCADE)
    namaMenu = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='images/', blank=True, default='images/default.jpg')
    rating_count = models.IntegerField(default=0)
    Deskripsi = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def average_rating(self):
        return self.rating_set.aggregate(Avg('rating'))['rating__avg'] or 0 

    def __str__(self):
        return self.namaMenu

@receiver(post_save, sender=Rating)
def update_menu_rating_count(sender, instance, created, **kwargs):
    if created:
        menu = instance.idmenu
        menu.rating_count = menu.rating_set.count()
        menu.save()


@receiver(post_save, sender=Rating)
def add_points_on_rating(sender, instance, created, **kwargs):
    if created:
        user = instance.idpengguna
        user.poin += 10
        user.save()

def get_recommendations(user):
    # Get all menus with at least one rating
    rated_menus = Menu.objects.annotate(avg_rating=Avg('rating__rating')).filter(avg_rating__isnull=False)

    # Order the menus by average rating in descending order
    recommended_menus = rated_menus.order_by('-avg_rating')

    return recommended_menus