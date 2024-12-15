from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Users, Menu, kategori, Location, Rating, Restoran, get_recommendations
from .forms import UserForm, UserFormlogin, UserFormupdate, UserFormupdatepassword, RatingCreateForm
from .filters import MenuFilter
from django.db.models import Avg, Count, Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

#crud untuk login dan register
def create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud:Login')
    else:
        form = UserForm()
    return render(request, 'Register.html', {'form': form})

def read(request):
    if request.method == 'POST':
        form = UserFormlogin(request.POST)
        if form.is_valid():
            name = request.POST.get('username')
            password = request.POST.get('password')
            try:
                user = Users.objects.get(username=name, password=password)
                return redirect('crud:homepage', user_id=user.idpengguna)
            except Users.DoesNotExist:
                messages.success(request, ("Email atau Password salah"))
    else:
        form = UserFormlogin()
    return render(request, 'login.html', {'form': form})

def update_user_profile(request, user_id):
    user = get_object_or_404(Users, idpengguna=user_id)
    if request.method == 'POST':
        form = UserFormupdate(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('crud:profile', user_id=user_id)
    else:
        form = UserFormupdate(instance=user)
    return render(request, 'update_user_profile.html', {'form': form})

def update_user_password(request, user_id):
    user = get_object_or_404(Users, idpengguna=user_id)
    if request.method == 'POST':
        form = UserFormupdatepassword(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = form.cleaned_data['password']  # Directly set the password
            user.save()
            messages.success(request, 'Password updated successfully!')
            return redirect('crud:Login')  
    else:
        form = UserFormupdatepassword(instance=user)
    return render(request, 'update_user_password.html', {'form': form})

def create_rating(request, menu_id):
    menu = get_object_or_404(Menu, idmenu=menu_id)
    if request.method == 'POST':
        form = RatingCreateForm(request.POST, request.FILES)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.idpengguna = Users.objects.get(idpengguna=request.user.id)
            rating.idmenu = menu
            rating.save()
            messages.success(request, 'Rating created successfully!')
            return redirect('crud:homepage', user_id=request.user.id)
    else:
        form = RatingCreateForm()
    return render(request, 'create_rating.html', {'form': form, 'menu': menu})

def menu_list(request):
    menus = Menu.objects.all().annotate(avg_rating=Avg('rating__rating'))
    menu_filter = MenuFilter(request.GET, queryset=menus)
    filtered_menus = menu_filter.qs
    context = {'menu_filter': menu_filter, 'menus': filtered_menus}
    return render(request, 'search_results.html', context)

def index(request, user_id=None):
    if user_id:
        try:
            custom_user = Users.objects.get(idpengguna=user_id)
            username = custom_user.username
            recommended_menus = get_recommendations(custom_user)
        except Users.DoesNotExist:
            custom_user = None
            username = None
            recommended_menus = []
    else:
        custom_user = None
        username = None
        recommended_menus = []
    context = {'user_id': user_id, 'username': username, 'recommended_menus': recommended_menus}
    return render(request, 'homepage.html', context)

def edit_profile(request, user_id):
    user = get_object_or_404(Users, idpengguna=user_id)
    if request.method == 'POST':
        form = UserFormupdate(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile', user_id=user_id)
    else:
        form = UserFormupdate(instance=user)
    return render(request, 'edit_profile.html', {'form': form})

def profile(request, user_id):
    user = get_object_or_404(Users, idpengguna=user_id)
    ratings = Rating.objects.filter(idpengguna=user)
    favorite_menus = Rating.objects.filter(idpengguna=user, rating__gt=4).values_list('idmenu', flat=True)
    favorite_menus = Menu.objects.filter(idmenu__in=favorite_menus)
    if not user.foto_profil:
        user.foto_profil = 'images/default.jpg'
    context = {
        'user': user,
        'ratings': ratings,
        'favorite_menus': favorite_menus,
    }
    return render(request, 'profile.html', context)

def rating_details(request, menu_id):
    menu = get_object_or_404(Menu, idmenu=menu_id)
    ratings = Rating.objects.filter(idmenu=menu).select_related('idpengguna')
    restaurant = get_object_or_404(Restoran, idrestoran=menu.idrestoran_id)
    context = {
        'menu': menu,
        'ratings': ratings,
        'restaurant': restaurant,
    }
    return render(request, 'rating_details.html', context)

def restaurant_details(request, restaurant_id):
    restaurant = get_object_or_404(Restoran, idrestoran=restaurant_id)
    menus = Menu.objects.filter(idrestoran=restaurant).annotate(avg_rating=Avg('rating__rating'))
    context = {
        'restaurant': restaurant,
        'menus': menus,
    }
    return render(request, 'restaurant_details.html', context)
    
    
