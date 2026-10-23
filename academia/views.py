from django.shortcuts import render

from .models import Modalidade, Turma


ORDEM_DIAS = {
    "segunda": 1,
    "terca": 2,
    "quarta": 3,
    "quinta": 4,
    "sexta": 5,
    "sabado": 6,
}


def inicio(request ):
    modalidades = Modalidade.objects.filter(ativa=True).order_by("nome")

    contexto = {
        "modalidades": modalidades,
        "nome_academia": "Academia incrivel hulk",
        "endereco": "Caruaru - PE",
        "telefone": "(81) 00000-0000",
    }

    return render(request, "academia/inicio.html", contexto)


def lista_turmas(request):
    turmas = list(
        Turma.objects.select_related("modalidade").all()
    )

    turmas.sort(
        key=lambda turma: (
            ORDEM_DIAS[turma.dia_semana],
            turma.horario,
        )
    )

    contexto = {
        "turmas": turmas,
        "nome_academia": "Academia Corpo em Movimento",
    }

    return render(request, "academia/turmas.html", contexto)