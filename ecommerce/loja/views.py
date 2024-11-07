from django.shortcuts import render
from .models import Produto

def lista_produtos(request):
    produtos = Produto.objects.all()
    print(produtos)
    return render(request, 'loja/lista_produtos.html', {'produtos': produtos})

from django.shortcuts import get_object_or_404

def detalhes_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'loja/detalhes_produto.html', {'produto': produto})
