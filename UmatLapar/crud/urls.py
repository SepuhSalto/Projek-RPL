from django.urls import path
from . import views

app_name = 'crud'

urlpatterns = [
    path('register/', views.create, name='Register'),
    path('login/', views.read, name='Login'),
    path('home/', views.index, name='homepage'),
    path('', views.index, name='landingpage'),
    path('search/', views.menu_list, name='menu_list'),
    path('recommend/<int:user_id>/', views.recommend_menus, name='recommend_menus')
]