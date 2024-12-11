from django.contrib import admin
from crud.models import Users, Rating, Restoran, Event, Menu, kategori, Location

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('idpengguna', 'username', 'email', 'poin', 'created_at', 'updated_at')
    search_fields = ('username', 'email')
    list_filter = ('created_at', 'updated_at')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('idrating', 'idpengguna', 'idmenu', 'rating', 'created_at', 'updated_at')
    search_fields = ('idpengguna__username', 'idmenu__namaMenu')
    list_filter = ('created_at', 'updated_at')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('idevent', 'namaevent', 'tanggal', 'lokasi', 'created_at', 'updated_at')
    search_fields = ('namaevent', 'lokasi')
    list_filter = ('tanggal', 'created_at')

@admin.register(Restoran)
class RestoranAdmin(admin.ModelAdmin):
    list_display = ('idrestoran', 'namaRestoran', 'waktuBuka', 'waktuTutup', 'alamat', 'created_at', 'updated_at')
    search_fields = ('namaRestoran', 'alamat')
    list_filter = ('created_at', 'updated_at')

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('idmenu', 'idrestoran', 'namaMenu', 'created_at', 'updated_at')
    search_fields = ('namaMenu', 'idrestoran__namaRestoran')
    list_filter = ('created_at', 'updated_at')
    
@admin.register(kategori)
class kategoriAdmin(admin.ModelAdmin):
    list_display = ('idkategori', 'kategori', 'created_at', 'updated_at')
    search_fields = ('kategori',)
    list_filter = ('created_at', 'updated_at')
    
@admin.register(Location)
class locationAdmin(admin.ModelAdmin):
    list_display = ('idlocation', 'lokasi', 'created_at', 'updated_at')
    search_fields = ('lokasi',)
    list_filter = ('created_at', 'updated_at')