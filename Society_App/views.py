from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Farmer
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import FarmerSignUpForm  # We will create this form
from .forms import FarmerForm  # We'll create this form next


@staff_member_required
def farmer_list(request):
    farmers = Farmer.objects.all()
    return render(request, 'farmers/farmer_list.html', {'farmers': farmers})

@login_required
def farmer_detail(request, pk):
    farmer = get_object_or_404(Farmer, pk=pk)
    return render(request, 'farmers/farmer_detail.html', {'farmer': farmer})

def farmer_register(request):
    if request.method == "POST":
        form = FarmerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('farmer_detail', pk=user.farmer.pk)  # Redirect to profile
    else:
        form = FarmerSignUpForm()
    
    return render(request, 'farmers/farmer_register.html', {'form': form})

@login_required
def farmer_update(request, pk):
    farmer = get_object_or_404(Farmer, pk=pk)

    if request.method == "POST":
        form = FarmerForm(request.POST, instance=farmer)
        if form.is_valid():
            form.save()
            return redirect('farmer_detail', pk=farmer.pk)
    else:
        form = FarmerForm(instance=farmer)

    return render(request, 'farmers/farmer_update.html', {'form': form})

@login_required
def farmer_delete(request, pk):
    farmer = get_object_or_404(Farmer, pk=pk)
    
    if request.method == "POST":
        user = farmer.user
        farmer.delete()
        user.delete()
        return redirect('home')  # Redirect to homepage after deletion

    return render(request, 'farmers/farmer_delete.html', {'farmer': farmer})

def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")
