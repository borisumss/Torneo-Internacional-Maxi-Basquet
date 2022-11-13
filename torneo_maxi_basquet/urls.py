"""torneo_maxi_basquet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from torneo import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('qr_code/', include('qr_code.urls', namespace="qr_code")),
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('administracion/torneos/crear', views.crear_torneo, name='crear_torneo'),
    path('administracion/torneos/editar/<int:id>', views.editar_torneo, name='editar_torneo'),
    path('administracion/', views.administracion, name='administracion'),
    path('administracion/torneos/', views.administracionTorneos, name='torneos'),
    path('administracion/torneos/baja/<int:id>', views.bajaTorneo, name='bajaTorneo'),
    path('administracion/equipos/', views.administracionEquipos, name='equipos'),
    path('MaxiBasket/equipos/<int:idequipo>', views.verEquipo, name='verEquipo'),
    path('administracion/torneos/terminados/', views.administracionTorneosTerminados, name='torneosTerminados'),
    path('administracion/solicitudes/', views.administracionSolicitudes, name='solicitudes'),
    path('administracion/delegados/', views.administracionDelegados, name='delegados'),
    path('administracion/delegados/baja/<str:tipo>/<int:id>', views.delegadosBaja, name='delegadosBaja'),
    path('administracion/delegados/alta/<str:tipo>/<int:id>', views.delegadosAlta, name='delegadosAlta'),
    path('delegacion/', views.delegacion, name='delegacion'),
    path('delegacion/Torneo', views.delegacionTorneo, name='delegacionTorneo'),
    path('delegacion/equipo', views.delegacionEquipo, name='delegacionEquipo'),
    path('delegacion/equipo/<int:id>/registrarJugador', views.inscribirEquipo, name='registrarJugador'),
    path('delegacion/equipo/<int:id>/registrarEntrenador', views.inscribirEntrenador, name='registrarEntrenador'),
    path('delegacion/credenciales', views.delegacionCredenciales, name='credenciales'),
    path('view_card/<int:pk>', views.view_card, name='view-card'),
    path('logout/', views.cerrarSesion, name='logout'),
    path('administracion/solicitudes/rechazadas/<str:tipo>/<int:id>', views.rechazar, name='Solicitud_Rechazada'),
    path('administracion/solicitudes/aceptadas/<str:tipo>/<int:id>', views.aceptar, name='Solicitud_Aceptada'),
    path('MaxiBasket/<int:id>', views.verTorneo, name='Torneo'),
    path('Torneos/', views.torneos, name='torneosTodos'),
    path('preinscripcion/<int:id>', views.preinscripcion, name='preinscripcion'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
