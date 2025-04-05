# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created. You can now log in.")
            return redirect("accounts:login") ### Remember to add "accounts:login" instead of "login" only
    else:
        form = RegistrationForm()
    return render(request, "products/register.html", {"form": form})

