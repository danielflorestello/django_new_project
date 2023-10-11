
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('principal/', views.principal, name='principal'),
    path('equipos/', views.equipos, name='equipos'),
    path('despachos/', views.despachos, name='despachos'),
    path('personal/', views.personal, name='personal'),
]
