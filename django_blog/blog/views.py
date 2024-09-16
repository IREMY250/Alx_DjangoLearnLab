

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required

# Login View
class CustomLoginView(LoginView):
    template_name = 'blog/login.html'

# Logout View
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('blog:login')

# Registration View
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'blog/register.html', {'form': form})

# Profile View (for authenticated users)
@login_required
def profile(request):
    return render(request, 'blog/profile.html')
