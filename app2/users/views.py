from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def register(request):
    """Регистрация нового пользователя."""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('tasks:task_list')
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    """Обработка входа пользователя."""
    if request.method != 'POST':
        form = AuthenticationForm()
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user is not None:
                login(request, user)
                return redirect('tasks:task_list')
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    """Выход пользователя."""
    logout(request)
    return render(request, 'registration/logged_out.html')
