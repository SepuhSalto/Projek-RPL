from django.urls import path
from . import views

app_name = 'crud'

urlpatterns = [
    path('register/', views.create, name='Register'),
    path('login/', views.read, name='Login'),
    path('home/', views.index, name='homepage'),
    path('', views.landing_page, name='landing_page'),
    path('search/', views.advanced_search, name='advanced_search'),
]