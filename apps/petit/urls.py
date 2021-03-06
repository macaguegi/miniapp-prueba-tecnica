from django.contrib import admin
from django.urls import path, include
from apps.petit import views
from django.contrib.auth.decorators import login_required


app_name = 'petit'

urlpatterns = [
    #path('inicio', views.inicio, name='inicio'),
    path('productos', views.listarProductos, name='listarProductos'),
    path('hacerOrden', views.hacerOrden, name='hacerOrden'),
    path('pagarOrden/<int:order_id>', views.pagarOrden, name='pagarOrden'),
    path('confirmarPago/<int:order_id>', views.confirmarPago, name='confirmarPago'),
    path('consultarTransacciones', login_required(views.consultarTransacciones), name='consultarTransacciones'),
    path('revertirTransaccion', login_required(views.revertirPago), name='revertirPago'),


]
