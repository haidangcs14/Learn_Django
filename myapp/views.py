from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
    # return HttpResponse('<h1>Hey, Welcome</h1>')
    # ft1 = Feature()
    # ft1.id = 0
    # ft1.name = 'Fast'
    # ft1.is_true = True
    # ft1.details = 'Our service is very quick'
    
    # ft2 = Feature()
    # ft2.id = 1
    # ft2.name = 'Reliable'
    # ft2.is_true = True
    # ft2.details = 'Our service is very reliable'
    
    # ft3 = Feature()
    # ft3.id = 2
    # ft3.name = 'Easy to use'
    # ft3.is_true = False
    # ft3.details = 'Our service is easy to use'
    
    # ft4 = Feature()
    # ft4.id = 3
    # ft4.name = 'Affordable'
    # ft4.is_true = True
    # ft4.details = 'Our service is very affordable'

    # fts = [ft1, ft2, ft3, ft4]
    fts = Feature.objects.all()

    return render(request, 'index.html', {'features': fts})

def counter(req):
    text = req.POST['text']
    amount_of_words = len(text.split())
    return render(req, 'counter.html', {'amount': amount_of_words})

def register(req):
    if req.method == 'POST':
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['password']
        password2 = req.POST['password2']

        if password == password2:
            pass
    return render(req, 'register.html')
