from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def crearTorneo(request):
    return render(request, 'crearTorneo.html')

def login(request):
    return render(request, 'login.html')

