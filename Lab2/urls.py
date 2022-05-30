"""Lab2 URL Configuration

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('Clients.urls')),
    path('home/', include('home.urls')),
    path('register', include('register.urls')),
    path('clientreg', include('clientreg.urls')),
    path('masterreg', include('masterreg.urls')),
    path('logincl', include('logincl.urls')),
    path('homeclient', include('homeClients.urls')),
    path('adddevices', include('AddDevices.urls')),
    path('loginmast', include('loginmast.urls')),
    path('homemaster', include('homeMasters.urls')),
    path('logout', include('logout.urls')),
]
