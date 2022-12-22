"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    path('', views.Noticias_base, name = 'home'),
    # Lo primero es el texto de la URL
    # Lo segundo es la vista que va a ejecutar
    # Lo tercero es el nombre de la URL (aun no lo usamos)


    path('Nosotros/', views.Nosotros, name = 'nosotros'),
    #No necesariamente estos 3 valores (Parametros) se deben llamar igual

    # LOGIN
    path('login/', auth.LoginView.as_view(template_name ='usuarios/login.html'),name='login'),
    path('logout/',auth.LogoutView.as_view(), name='logout'),

    # URL DE APLICACION
    path('Noticias/', include('apps.noticias.urls')),
    path('Usuario/', include('apps.usuarios.urls')),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    