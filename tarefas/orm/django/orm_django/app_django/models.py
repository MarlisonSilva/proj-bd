from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=150)
    sexo = models.CharField(max_length=1)
    dt_nasc = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    supervisor = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='subordinados')
    depto = models.ForeignKey('Departamento', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome

class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10, unique=True)
    descricao = models.CharField(max_length=250)
    gerente = models.ForeignKey(Funcionario, null=True, blank=True, on_delete=models.SET_NULL, related_name='departamentos_gerenciados')

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.CharField(max_length=250)
    responsavel = models.ForeignKey(Funcionario, null=True, blank=True, on_delete=models.SET_NULL)
    depto = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.SET_NULL)
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    descricao = models.CharField(max_length=250)
    projeto = models.ForeignKey(Projeto, null=True, blank=True, on_delete=models.SET_NULL)
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return f"{self.descricao[:30]}..."

