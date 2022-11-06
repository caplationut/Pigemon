"""Pigemon URL Configuration

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
from django.contrib import admin
from django.urls import path, include
import debug_toolbar
import breeder.views
import loft.views
import pigeon.views

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    # Auth links
    path('login/', loft.views.LoginPage.as_view(redirect_authenticated_user=True), name='login'),

    # Breeder links
    path('', breeder.views.index, name='index'),

    # Loft links
    path('new-loft/', loft.views.new_loft, name='new-loft'),

    # Pigeon links
    path('new-pigeon/', pigeon.views.add_pigeon, name='new-pigeon'),
    path('pigeons/', pigeon.views.view_pigeons, name='pigeons'),
    path('edit/pigeon/<int:pk>/', pigeon.views.edit_pigeon, name='edit-pigeon')
]
