from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'home/index.html')

def loja(request):
    return render(request, 'home/loja.html')
