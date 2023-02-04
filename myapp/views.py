from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    # return HttpResponse('<h1>Hey, Welcome</h1>')
    ft1 = Feature()
    ft1.id = 0
    ft1.name = 'Fast'
    ft1.details = 'Our service is very quick'
    return render(request, 'index.html', {'feature': ft1})

def counter(req):
    text = req.POST['text']
    amount_of_words = len(text.split())
    return render(req, 'counter.html', {'amount': amount_of_words})