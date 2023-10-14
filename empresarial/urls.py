from django.urls import path
from . import views

urlpatterns = [
    path('gerenciar_clientes/', views.gerenciar_clientes, name="gerenciar_clientes"),
    path('cliente/<int:cliente_id>', views.cliente, name="cliente"),
    path('exame_cliente/<int:exame_id>', views.exame_cliente, name="exame_cliente"),
]