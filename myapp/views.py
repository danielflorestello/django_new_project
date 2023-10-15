from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'index.html')


@login_required
def principal(request):
    return render(request, 'empleado/principal.html')


@login_required
def equipos(request):
    return render(request, 'empleado/equipos.html')


@login_required
def recomendacion(request):
    return render(request, 'empleado/recomendacion.html')


@login_required
def admin_principal(request):
    return render(request, 'administrador/admin_principal.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])

                user.save()

                login(request, user)

                return redirect('principal')

            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': "Username already exist"
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': "Password do not match"
        })


def signin(request):
    user = authenticate(
        request, username=request.POST['username'], password=request.POST['password'])

    if user is None:
        return render(request, 'index.html', {
            'error': "Usuario o contraseña incorrecta"
        })

    else:
        login(request, user)
        return redirect('principal')


@login_required
def signout(request):
    logout(request)
    return redirect('index')
