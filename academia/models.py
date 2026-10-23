from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Modalidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Turma(models.Model):
    DIAS_DA_SEMANA = [
        ("segunda", "Segunda"),
        ("terca", "Terça"),
        ("quarta", "Quarta"),
        ("quinta", "Quinta"),
        ("sexta", "Sexta"),
        ("sabado", "Sábado"),
    ]

    modalidade = models.ForeignKey(
        Modalidade,
        on_delete=models.PROTECT,
        related_name="turmas",
    )
    dia_semana = models.CharField(
        max_length=10,
        choices=DIAS_DA_SEMANA,
    )
    horario = models.TimeField()
    instrutor = models.CharField(max_length=100)
    vagas = models.PositiveIntegerField(
        validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return f"{self.modalidade} - {self.dia_semana} - {self.horario}"