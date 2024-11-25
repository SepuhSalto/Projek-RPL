from django.shortcuts import render, redirect, get_object_or_404
from .models import Users
from .forms import UserForm

# Create a new user
def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = UserForm()
    return render(request, 'Register.html', {'form': form})

