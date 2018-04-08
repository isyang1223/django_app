"""django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^time_display', include('apps.time_display.urls')), #this goes to localhost:800/time_display
    url(r'^random_word', include('apps.random_word.urls')), #this goes to localhost:8000/random_word
    url(r'^amadon', include('apps.amadon.urls')),
    url(r'^', include('apps.blogs.urls')), #this goes to localhost:8000 root
]
