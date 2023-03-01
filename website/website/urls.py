"""website URL Configuration

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
from django.urls import include, path
from core.views import index # import the index function from core/views.py
from core.views import portfolio
from core.views import contact
from core.views import about
from core.views import services

urlpatterns = [
    path('', index, name='index'), # add the index function to the urlpatterns list
    path('portfolio/', portfolio, name='portfolio'), # add the portfolio function to the urlpatterns list
    path('contact/', contact, name='contact'), # add the contact function to the urlpatterns list
    path('about/', about, name='about'), # add the contact function to the urlpatterns list
    path('services/', services, name='services'), # add the contact function to the urlpatterns list

    path('admin/', admin.site.urls),
    # path('services/', services, name='services'),
    path("__reload__/", include("django_browser_reload.urls")),
]
