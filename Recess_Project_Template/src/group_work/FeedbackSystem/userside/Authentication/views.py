from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.templatetags.static import static


def home(request):
    return render(request, 'Authentication/home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'Authentication/register.html', {'form': form})

def images(request):
    egg_yolk_url = static('Authentication/images/egg_yolk.png')
    return render(request, 'base.html', {'egg_yolk_url': egg_yolk_url})


@login_required()
def profile(request):
    return render(request, 'Authentication/profile.html')
