from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime

  # the index function is called when root is visited
def index(request):
    context = {
        "time": strftime("%I:%M %p %a", localtime()),
        "date": strftime("%m-%d-%Y", localtime()),
    }
    return render(request,'time_display/index.html', context)