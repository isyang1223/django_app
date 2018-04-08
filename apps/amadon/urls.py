from django.conf.urls import url
from . import views        
   # This line is new!
urlpatterns = [
    url(r'^$', views.index),  #this goes to localhost:8000/amadon
    url(r'^/process$', views.process), 
    url(r'^/checkout$', views.checkout),
    url(r'^/reset$', views.reset),
    ]