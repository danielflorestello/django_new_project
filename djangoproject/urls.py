
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    # -------------------------------------------------------------------------------

    path('principal/', views.principal, name='principal'),
    path('equipos/', views.equipos, name='equipos'),
    path('recomendacion/', views.recomendacion, name='recomendacion'),

    # -------------------------------------------------------------------------------

    path('administrador/principal', views.admin_principal, name='admin_principal'),
    path('administrador/servicios', views.servicios, name='servicios'),
    path('administrador/agregarServicios', views.agregarServicios, name='agregarServicios'),
    path('administrador/usuarios', views.usuarios, name='usuarios'),
    path('administrador/tipos', views.tipos_equipos, name='tipos_equipos'),
    path('administrador/agregarTipos', views.agregarTipos, name='agregarTipos'),

    # --------------------------------------------------------------------------------

    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)