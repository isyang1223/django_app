from django.conf.urls import url
from . import views        
   # This line is new!
urlpatterns = [
    url(r'^$', views.index),  #this goes to localhost:8000/random_word
    url(r'^/reset$', views.reset),     # this goes to localhost:8000/random_word/reset
    ]