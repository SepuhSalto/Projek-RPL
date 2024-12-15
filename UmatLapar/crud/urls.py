from django.urls import path
from . import views

app_name = 'crud'

urlpatterns = [
    path('register/', views.create, name='Register'),
    path('login/', views.read, name='Login'),
    path('home/<int:user_id>', views.index, name='homepage'),
    path('', views.index, name='landingpage'),
    path('search/', views.menu_list, name='menu_list'),
    path('create_rating/<int:menu_id>/', views.create_rating, name='create_rating'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('rating_details/<int:menu_id>/', views.rating_details, name='rating_details'),
    path('restaurant_details/<int:restaurant_id>/', views.restaurant_details, name='restaurant_details'),
    path('update_user_profile/<int:user_id>/', views.update_user_profile, name='update_user_profile'),
]