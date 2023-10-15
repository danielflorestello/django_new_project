
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('principal/', views.principal, name='principal'),
    path('equipos/', views.equipos, name='equipos'),
    path('recomendacion/', views.recomendacion, name='recomendacion'),
    path('administrador/principal', views.admin_principal, name='admin_principal'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),
]
