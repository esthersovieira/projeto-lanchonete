from django.urls import include, path
from django.contrib import admin
from home import views as home_views

urlpatterns = [   
    path ('', home_views.index, name='index'),
    path('home/', include('home.urls')),
    path('cardapio/', include('cardapio.urls')),
    path('produtos/', include('produtos.urls')),
    path('pedidos/', include ('pedidos.urls')),
    path('admin/', admin.site.urls),
]
