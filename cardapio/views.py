from django.shortcuts import render

# Create your views here.
def cardapio(x = None):
    return render(x, 'cardapio/index.html')
