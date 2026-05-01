from django.shortcuts import render

# Create your views here.
def pedidos(x = None):
    return render(x, 'pedidos/index.html')
