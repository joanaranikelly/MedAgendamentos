from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

class Usuario(AbstractUser):
    TIPO_USUARIO_CHOICES = [
        ('P', 'Paciente'),
        ('R', 'Recepcionista'),
        ('M', 'Profissional de Saúde'),
        ('A', 'Administrador da Clínica'),
        ('S', 'Super Administrador')
    ]
    tipo_usuario = models.CharField(max_length=1, choices=TIPO_USUARIO_CHOICES)
    clinica = models.ForeignKey('Clinica', on_delete=models.SET_NULL, null=True, blank=True)

class Clinica(models.Model):
    nome = models.CharField(max_length=100, default="")
    endereco = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.nome

class Paciente(models.Model):
    nome =models.CharField(max_length=200, default="")
    data_de_nascimento = models.DateField()
    endereco = models.CharField(max_length=200)

    @property
    def idade(self):
        if self.data_de_nascimento:
            hoje = date.today()
            idade = hoje.year - self.data_de_nascimento.year
            if (hoje.month, hoje.day) < (self.data_de_nascimento.month, self.data_de_nascimento.day):
                idade -= 1
            return idade
        return None

    def __str__(self):
        return f"{self.nome} ({self.idade} anos)"

class ProfissionalSaude(models.Model):
    nome =models.CharField(max_length=200, default="")
    especialidade = models.CharField(max_length=50)
    clinicas = models.ManyToManyField(Clinica) 

    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.last_name} - {self.especialidade}"


class Recepcionista(models.Model):
    nome =models.CharField(max_length=200, default="")
    endereco = models.CharField(max_length=200)
    clinicas = models.ManyToManyField(Clinica)
    data_contratacao = models.DateField()

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profissional_saude = models.ForeignKey(ProfissionalSaude, on_delete=models.CASCADE)
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    status_choices = [
        ('P', 'Pendente'),
        ('C', 'Confirmada'),
        ('R', 'Realizada'),
        ('X', 'Cancelada'),
    ]
    status = models.CharField(max_length=1, choices=status_choices, default='P')
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Consulta de {self.paciente.nome} com {self.profissional_saude.usuario.first_name} em {self.data_hora.strftime('%d/%m/%Y %H:%M')}"

    class Meta:
        ordering = ['data_hora']