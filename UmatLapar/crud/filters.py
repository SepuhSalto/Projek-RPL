import django_filters
from .models import Menu, Restoran,kategori, Location
from django.db.models import Avg

class MenuFilter(django_filters.FilterSet):
    namaMenu = django_filters.CharFilter(
        field_name='namaMenu',
        lookup_expr='icontains',
        label='Nama Menu'
    )
    idrestoran__namaRestoran = django_filters.CharFilter(
        field_name='idrestoran__namaRestoran',
        lookup_expr='icontains',
        label='Nama Restoran'
    )
    rating = django_filters.NumberFilter(method='filter_by_rating', label='Rating')
    location = django_filters.ChoiceFilter(
        field_name='idrestoran__idlocation__lokasi',
        lookup_expr='icontains',
        choices=[(location.lokasi, location.lokasi) for location in Location.objects.all()],
        label='Lokasi'
    )
    idkategori__kategori = django_filters.ChoiceFilter(
        field_name='idkategori__kategori',
        lookup_expr='exact',
        choices=[(kategori.kategori, kategori.kategori) for kategori in kategori.objects.all()],
        label='Kategori'
    )
    def filter_by_rating(self, queryset, name, value):
        if value:
            queryset = queryset.annotate(avg_rating=Avg('rating__rating'))
            queryset = queryset.filter(avg_rating__gte=value)
        return queryset
    class Meta:
        model = Menu
        fields = {
            'idkategori__kategori': ['exact'],
        }

   