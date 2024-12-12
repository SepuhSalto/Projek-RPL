from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Users, Menu, kategori, Location, Rating, get_recommendations
from .forms import UserForm, UserFormlogin, UserFormupdate, UserFormupdatepassword, RatingCreateForm
from .filters import MenuFilter
from django.db.models import Avg, Count, Q
from django.core.paginator import Paginator

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
            name = request.POST.get('name')
            password = request.POST.get('password')
            
            try:
                user = Users.objects.get(name=name, password=password)
                return redirect('crud:homepage')
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
            return redirect('profile', user_id=user_id)
    else:
        form = UserFormupdate(instance=user)
    return render(request, 'update_user_profile.html', {'form': form})

def update_user_password(request, user_id):
    user = get_object_or_404(Users, idpengguna=user_id)
    if request.method == 'POST':
        form = UserFormupdatepassword(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  
            user.save()
            messages.success(request, 'Password updated successfully!')
            return redirect('login')  
    else:
        form = UserFormupdatepassword(instance=user)
    return render(request, 'update_user_password.html', {'form': form})

def create_rating(request):
    if request.method == 'POST':
        form = RatingCreateForm(request.POST, request.FILES)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.idpengguna = request.user  
            rating.save()
            messages.success(request, 'Rating created successfully!')
            return redirect('ratings_list')  
    else:
        form = RatingCreateForm()
    return render(request, 'create_rating.html', {'form': form})

def menu_list(request):
    menus = Menu.objects.all()
    menu_filter = MenuFilter(request.GET, queryset=menus)
    context = {'menu_filter': menu_filter}
    return render(request, 'search_results.html', context) 

def recommend_menus(request, user_id):
    user = get_object_or_404(Users, idpengguna=user_id)
    recommended_menus = get_recommendations(user)
    context = {'user': user, 'menus': recommended_menus}
    return render(request, 'recommendations.html', context)

def index(request):
    return render(request, 'homepage.html')
