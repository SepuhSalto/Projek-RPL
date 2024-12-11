from django.test import TestCase
from django.db.models import Avg, Count
from .models import Menu, kategori, Location, Rating, Restoran, Users

class SearchRecommendationTest(TestCase):
    def setUp(self):
        # Create test data
        self.location = Location.objects.create(
            lokasi="Test Location"
        )
        
        self.category = kategori.objects.create(
            kategori="Test Category"
        )
        
        self.restaurant = Restoran.objects.create(
            idlocation=self.location,
            namaRestoran="Test Restaurant",
            waktuBuka="08:00",
            waktuTutup="22:00",
            alamat="Test Address",
            hargaTerkecil=10000,
            hargaTerbesar=50000
        )
        
        self.menu = Menu.objects.create(
            idkategori=self.category,
            idrestoran=self.restaurant,
            namaMenu="Test Menu"
        )
        
        self.user = Users.objects.create(
            username="testuser",
            email="test@test.com",
            password="testpass"
        )
        
        # Create some ratings
        Rating.objects.create(
            idpengguna=self.user,
            idmenu=self.menu,
            rating=5
        )

    def test_search_by_category(self):
        results = Menu.objects.annotate(
            avg_rating=Avg('rating__rating')
        ).filter(idkategori=self.category)
        
        self.assertEqual(results.count(), 1)
        self.assertEqual(results[0].namaMenu, "Test Menu")

    def test_search_by_location(self):
        results = Menu.objects.annotate(
            avg_rating=Avg('rating__rating')
        ).filter(idrestoran__idlocation=self.location)
        
        self.assertEqual(results.count(), 1)
        self.assertEqual(results[0].idrestoran.namaRestoran, "Test Restaurant")

    def test_combined_search(self):
        results = Menu.objects.annotate(
            avg_rating=Avg('rating__rating')
        ).filter(
            namaMenu__icontains="Test",
            idkategori=self.category,
            idrestoran__idlocation=self.location
        )
        
        self.assertEqual(results.count(), 1)
        self.assertEqual(results[0].avg_rating, 5.0)

    def test_recommendation_ordering(self):
        # Create another menu with lower rating
        menu2 = Menu.objects.create(
            idkategori=self.category,
            idrestoran=self.restaurant,
            namaMenu="Test Menu 2"
        )
        
        Rating.objects.create(
            idpengguna=self.user,
            idmenu=menu2,
            rating=3
        )
        
        results = Menu.objects.annotate(
            avg_rating=Avg('rating__rating')
        ).order_by('-avg_rating')
        
        self.assertEqual(results[0].namaMenu, "Test Menu")  # Higher rated
        self.assertEqual(results[1].namaMenu, "Test Menu 2")  # Lower rated