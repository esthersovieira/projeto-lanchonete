from django.shortcuts import render

# Create your views here.
def produtos(x = None):
    return render(x, 'produtos/index.html')
