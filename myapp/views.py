from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Servicio, Tipo
import pandas as pd

# Create your views here.


def index(request):
    return render(request, 'index.html')


# --------------------------------------------------------------------


@login_required
def principal(request):
    return render(request, 'empleado/principal.html')


@login_required
def equipos(request):
    file_path = 'A143_ALMACEN PINT-PMO - REDYCOM.xlsm'
    df = pd.read_excel(file_path, engine='openpyxl')

    data = df[['DESCRIPCION', 'CAN']]
    
    return render(request, 'empleado/equipos.html', {'data': data})


@login_required
def recomendacion(request):
    return render(request, 'empleado/recomendacion.html')


# ------------------------------------------------------------------


@login_required
def admin_principal(request):
    return render(request, 'administrador/admin_principal.html')


@login_required
def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'administrador/servicios/servicios.html', {'servicios': servicios})

@login_required
def agregarServicios(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')

        if nombre:
            Servicio.objects.create(nombre=nombre)
            return JsonResponse({'success': True})  # Devuelve una respuesta JSON de éxito
            
    return JsonResponse({'success': False})  # Devuelve una respuesta JSON de error


@login_required
def usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'administrador/usuarios/usuarios.html', {'usuarios': usuarios})


@login_required
def tipos_equipos(request):
    tipos = Tipo.objects.all()
    return render(request, 'administrador/tipos/tipos.html', {'tipos': tipos})


@login_required
def agregarTipos(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        imagen = request.FILES.get('imagen')

        try:
            Tipo.objects.create(nombre=nombre, imagen=imagen)
            return JsonResponse({'success': True})  # Devuelve una respuesta JSON de éxito
        
        except:
            return JsonResponse({'success': False})  # Devuelve una respuesta JSON de error
        
    else:
        return JsonResponse({'success': False})  # Devuelve una respuesta JSON de error

# -------------------------------------------------------------------


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
