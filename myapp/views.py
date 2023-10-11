from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def principal(request):
    return render(request, 'principal.html')

def equipos(request):
    return render(request, 'equipos.html')

def despachos(request):
    return render(request, 'despachos.html')

def personal(request):
    return render(request, 'personal.html')