from django.shortcuts import render, HttpResponse, redirect


  # the index function is called when root is visited
def index(request):

    
    return render(request,'amadon/index.html')
def process(request):
    if request.method == 'POST':
        if not "todaycharged" in request.session:
            request.session['todaycharged'] = 0
        if not "totalcharged" in request.session:
            request.session['totalcharged'] = 0
        if not "totalitem" in request.session:
            request.session['totalitem'] = 0 

        if request.POST['product'] == 'shirt':
            price = 19.99
        elif request.POST['product'] == 'sweater':
            price = 29.99
        elif request.POST['product'] == 'cup':
            price = 4.99
        elif request.POST['product'] == 'book':
            price = 49.99
    
    request.session['todaycharged'] = price * int(request.POST['quantity'])
    request.session['totalcharged'] += request.session['todaycharged']
    request.session['totalitem'] += int(request.POST['quantity'])


    return redirect('/amadon/checkout')

def reset(request):
    print"hiiiiii"
    request.session.clear()
    
    return redirect('/amadon')

def checkout(request):
    
    
    return render(request,'amadon/checkout.html')