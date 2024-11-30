from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Users
from .forms import UserForm, UserFormlogin

# crud untuk login dan register
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

def index(request):
    return render(request, 'homepage.html')
