from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Servicio, Tipo
import pandas as pd
import os

# Create your views here.


def index(request):
    return render(request, 'index.html')


# --------------------------------------------------------------------


@login_required
def principal(request):
    servicios = Servicio.objects.all()
    tipos = Tipo.objects.all()
    return render(request, 'empleado/principal.html', {
        'servicios': servicios,
        'tipos': tipos
    })


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


# ------------------------------------------------------------------


@login_required
def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'administrador/servicios/servicios.html', {'servicios': servicios})


@login_required
def agregarServicios(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')

        if nombre:
            servicio = Servicio.objects.create(nombre=nombre)
            servicio.save()

            # Devuelve una respuesta JSON de éxito
            return JsonResponse({'success': True})

    else:
        # Devuelve una respuesta JSON de error
        return JsonResponse({'success': False})


@login_required
def editarServicios(request, servicio_id):
    if request.method == 'GET':
        servicio = Servicio.objects.get(id=servicio_id)
        return render(request, 'administrador/servicios/editarServicio.html', {
            'servicio': servicio
        })

    else:
        try:
            nombre = request.POST.get('nombre')

            servicios = Servicio.objects.get(id=servicio_id)
            servicios.nombre = nombre
            servicios.save()

            return redirect('servicios')

        except ValueError:
            return render(request, 'administrador/servicios/servicios.html', {
                'servicios': servicios,
                'error': 'Error al actualizar el servicio'
            })


@login_required
def eliminarServicios(request, servicio_id):
    servicio = get_object_or_404(Servicio, pk=servicio_id)
    servicio.delete()
    return JsonResponse({'success': True})


# ------------------------------------------------------------------


@login_required
def usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'administrador/usuarios/usuarios.html', {'usuarios': usuarios})


@login_required
def agregarUsuarios(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if first_name and last_name and email and username and password:
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )

            user.save()

            grupo = Group.objects.get(name='usuario')
            user.groups.add(grupo)

            return JsonResponse({'success': True})

    else:
        return JsonResponse({'success': False})


@login_required
def editarUsuarios(request, usuario_id):
    if request.method == 'GET':
        usuario = User.objects.get(id=usuario_id)
        return render(request, 'administrador/usuarios/editarUsuario.html', {
            'usuario': usuario
        })

    else:
        try:
            first_name = request.POST.get('nombre')
            last_name = request.POST.get('apellido')
            username = request.POST.get('username')
            email = request.POST.get('correo')

            usuarios = User.objects.get(id=usuario_id)
            usuarios.first_name = first_name
            usuarios.last_name = last_name
            usuarios.username = username
            usuarios.email = email
            usuarios.save()

            return redirect('usuarios')

        except ValueError:
            return render(request, 'administrador/usuarios/usuarios.html', {
                'usuarios': usuarios,
                'error': 'Error al actualizar el usuario'
            })


@login_required
def eliminarUsuarios(request, usuario_id):

    user = get_object_or_404(User, pk=usuario_id)
    group = Group.objects.get(user=user)

    user.groups.remove(group)
    user.delete()

    return JsonResponse({'success': True})


# ------------------------------------------------------------------


@login_required
def tipos_equipos(request):
    tipos = Tipo.objects.all()
    return render(request, 'administrador/tipos/tipos.html', {'tipos': tipos})


@login_required
def agregarTipos(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        imagen = request.FILES.get('imagen')

        if nombre and imagen:
            tipo = Tipo.objects.create(nombre=nombre, imagen=imagen)
            tipo.save()
            # Devuelve una respuesta JSON de éxito
            return JsonResponse({'success': True})

    else:
        # Devuelve una respuesta JSON de error
        return JsonResponse({'success': False})


@login_required
def editarTipos(request, tipo_id):
    if request.method == 'GET':
        tipo = Tipo.objects.get(id=tipo_id)
        return render(request, 'administrador/tipos/editarTipo.html', {
            'tipo': tipo
        })

    else:
        try:
            nombre = request.POST.get('nombre')
            imagen = request.FILES.get('imagen')

            tipos = get_object_or_404(Tipo, pk=tipo_id)

            if imagen:

                if tipos.imagen:
                    os.remove(tipos.imagen.path)

                tipos.imagen = imagen

            tipos.nombre = nombre
            tipos.save()

            return redirect('tipos_equipos')

        except ValueError:
            return render(request, 'administrador/tipos/tipos.html', {
                'tipos': tipos,
                'error': 'Error al actualizar el tipo de equipo'
            })


@login_required
def eliminarTipos(request, tipo_id):
    tipo = get_object_or_404(Tipo, pk=tipo_id)

    if tipo.imagen:

        if os.path.exists(tipo.imagen.path):
            os.remove(tipo.imagen.path)

    tipo.delete()
    return JsonResponse({'success': True})


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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            user = User.objects.get(username=username)

            grupo = Group.objects.get(name='usuario')

            if user.groups.filter(name=grupo):
                return redirect('principal')

            else:
                return redirect('admin_principal')

        else:
            return render(request, 'index.html')

    else:
        return render(request, 'index.html', {
            'error': "Usuario o contraseña incorrecta"
        })


@login_required
def signout(request):
    logout(request)
    return redirect('index')
