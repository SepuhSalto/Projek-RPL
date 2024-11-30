from django.urls import path
from . import views

app_name = 'crud'

urlpatterns = [
    path('register/', views.create, name='Register'),
    path('login/', views.read, name='Login'),
    path('home/', views.index, name='homepage'),
]