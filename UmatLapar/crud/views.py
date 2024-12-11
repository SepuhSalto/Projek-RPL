from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Users
from .forms import UserForm, UserFormlogin, UserFormupdate, UserFormupdatepassword, RatingCreateForm
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

def landing_page(request):
    # Get top rated menus for recommendations
    recommended_menus = Menu.objects.annotate(
        avg_rating=Avg('rating__rating'),
        rating_count=Count('rating')
    ).filter(
        rating_count__gte=1
    ).order_by('-avg_rating', '-rating_count')[:8]

    # Get all categories and locations for search filters
    categories = kategori.objects.all()
    locations = Location.objects.all()

    context = {
        'recommended_menus': recommended_menus,
        'categories': categories,
        'locations': locations,
    }
    return render(request, 'landing_page.html', context)

def advanced_search(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', '')
    location_id = request.GET.get('location', '')

    # Start with all menus
    menu_results = Menu.objects.annotate(
        avg_rating=Avg('rating__rating'),
        rating_count=Count('rating')
    )

    # Apply filters based on search criteria
    if query:
        menu_results = menu_results.filter(
            Q(namaMenu__icontains=query) |
            Q(idrestoran__namaRestoran__icontains=query)
        )

    if category_id:
        menu_results = menu_results.filter(idkategori_id=category_id)

    if location_id:
        menu_results = menu_results.filter(idrestoran__idlocation_id=location_id)

    # Order by rating
    menu_results = menu_results.order_by('-avg_rating', '-rating_count')

    context = {
        'menu_results': menu_results,
        'query': query,
        'selected_category': category_id,
        'selected_location': location_id,
        'categories': kategori.objects.all(),
        'locations': Location.objects.all(),
    }
    return render(request, 'search_results.html', context)

def index(request):
    return render(request, 'homepage.html')
