from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import TiposExames, PedidosExames, SolicitacaoExame
from datetime import datetime
from django.contrib import messages
from django.contrib.messages import constants


@login_required  # É uma propriedade que faz chamar esta função somente quando o usuario estiver logado
def solicitar_exames(request):
    if request.method == "GET":
        tipos_exames = TiposExames.objects.all()
        return render(request, "solicitar_exames.html", {"tipos_exames": tipos_exames})
    elif request.method == "POST":
        exames_id = request.POST.getlist("exames")
        tipos_exames = TiposExames.objects.all()
        solicitacao_exames = TiposExames.objects.filter(
            id__in=exames_id
        )  # id__in 34:20 (se os id estiverem dentro desta lista traga para variavel)

        preco_total = 0
        for i in solicitacao_exames:
            if i.disponivel:
                preco_total += i.preco

        return render(
            request,
            "solicitar_exames.html",
            {
                "tipos_exames": tipos_exames,
                "solicitacao_exames": solicitacao_exames,
                "preco_total": preco_total,
            },
        )


@login_required
def fechar_pedido(request):
    exames_id = request.POST.getlist("exames")
    solicitacao_exames = TiposExames.objects.filter(id__in=exames_id)

    pedido_exame = PedidosExames(
        usuario=request.user,
        data=datetime.now(),
    )

    pedido_exame.save()

    for exame in solicitacao_exames:
        solicitacao_exames_temp = SolicitacaoExame(
            usuario=request.user, exame=exame, status="E"
        )

        solicitacao_exames_temp.save()
        pedido_exame.exames.add(solicitacao_exames_temp)
    pedido_exame.save()
    messages.add_message(
        request, constants.SUCCESS, "Pedido de exame realizado com sucesso"
    )
    return redirect("/exames/gerenciar_pedidos")


def gerenciar_pedidos(request):
    pedidos_exames = PedidosExames.objects.filter(usuario=request.user)

    return render(request, "gerenciar_pedidos.html", {"pedidos_exames": pedidos_exames})
