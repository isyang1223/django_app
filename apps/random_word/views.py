from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

  # the index function is called when root is visited
def index(request):
    if not 'count' in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1

    context = {
        "randomstring": get_random_string(length=14),
        "header": "Random Word (attempt #" + str(request.session['count']) + ")"
        }
    
    return render(request,'random_word/index.html', context)

def reset(request):
    if request.method == "POST":
        request.session['count'] = 0
    
    return redirect('/random_word')