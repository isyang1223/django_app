from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),  #this goes to localhost:8000 root
    url(r'^new$', views.new),  #this goes to localhost:8000/new
    url(r'^create$', views.create),  #this goes to localhost:8000/create
    url(r'^(?P<number>\d+)$', views.show), #this goes to localhost:8000/<anynumber>
    url(r'^(?P<number>\d+)/edit$', views.edit), #this goes to localhost:8000/<anynumber>/edit
    url(r'^(?P<number>\d+)/delete$', views.delete) #this goes to localhost:8000/<anynumber>/delete
]