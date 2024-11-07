# ecommerce/loja/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),  # URL para lista de produtos
    path('produto/<int:produto_id>/', views.detalhes_produto, name='detalhes_produto'),  # URL para detalhes do produto
]
