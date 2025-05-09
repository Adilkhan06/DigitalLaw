"""
URL configuration for digitallaw project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from terms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('term/<int:term_id>/', views.term_detail, name='term_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('references/', views.references, name='references'),
    path('contact/', views.contact, name='contact'),
    path('reviews/', views.reviews, name='reviews'),
    path('google-search/', views.google_search, name='google_search'),
]