"""Aturnos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from apps.turnos.views import turn,createTurn,editTurn,deleteTurn
from apps.Users.Profiles.views import data,createUser,editUser,deleteUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('turno/',turn,name='turno'),
    path('',data,name='index'),
    path('crearUser/',createUser,name='crear_user'),
    path('crearTurno/',createTurn,name='crear_turno'),
    path('editarUser/<int:id>/',editUser, name = 'editar_user'),
    path('eliminarUser/<int:id>/',deleteUser, name = 'eliminar_user'),  
    path('eliminarTurno/<int:id>/',deleteTurn, name = 'eliminar_turno'),  
    path('editarTurno/<int:id>/',editTurn, name = 'editar_turno'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # Para poder mostrar la imagen