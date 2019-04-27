from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView, UpdateView
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account created! You are now able to log in.')
            return redirect('TodoList')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})
