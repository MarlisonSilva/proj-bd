from datetime import date
from decimal import Decimal
from app_django.models import Departamento, Funcionario, Projeto, Atividade

# Limpa dados anteriores (cuidado em produção!)
Atividade.objects.all().delete()
Projeto.objects.all().delete()
Funcionario.objects.all().delete()
Departamento.objects.all().delete()

# ------------------------------
# Departamentos
# ------------------------------
d1 = Departamento.objects.create(sigla='DHC', descricao='Dep. História')
d2 = Departamento.objects.create(sigla='DCT', descricao='Dep. Computação')
d3 = Departamento.objects.create(sigla='DGC', descricao='Dep. Geografia')
d4 = Departamento.objects.create(sigla='DIR', descricao='Dep. Direito')

# ------------------------------
# Funcionários Gerentes
# ------------------------------
f1 = Funcionario.objects.create(nome='Ana', sexo='F', dt_nasc=date(1988, 5, 7), salario=Decimal('2500.00'), depto=d1)
f2 = Funcionario.objects.create(nome='Taciano', sexo='M', dt_nasc=date(1980, 1, 25), salario=Decimal('2500.00'), depto=d2)

# Atualiza os gerentes dos departamentos
d1.gerente = f1
d1.save()
d2.gerente = f2
d2.save()

# ------------------------------
# Demais Funcionários
# ------------------------------
f3 = Funcionario.objects.create(nome='Maria', sexo='F', dt_nasc=date(1981, 7, 1), salario=Decimal('2500.00'), supervisor=f1, depto=d1)
f4 = Funcionario.objects.create(nome='Josefa', sexo='F', dt_nasc=date(1986, 9, 17), salario=Decimal('2500.00'), supervisor=f1, depto=d1)
f5 = Funcionario.objects.create(nome='Carlos', sexo='M', dt_nasc=date(1985, 11, 21), salario=Decimal('2500.00'), supervisor=f1, depto=d1)
f6 = Funcionario.objects.create(nome='José', sexo='M', dt_nasc=date(1979, 7, 12), salario=Decimal('3500.00'), supervisor=f2, depto=d2)
f7 = Funcionario.objects.create(nome='Gabriel', sexo='M', dt_nasc=date(1981, 8, 11), salario=Decimal('1850.00'), depto=d3)
f8 = Funcionario.objects.create(nome='Margarete', sexo='F', dt_nasc=date(1992, 3, 22), salario=Decimal('4500.00'), depto=d3)
f9 = Funcionario.objects.create(nome='José', sexo='M', dt_nasc=date(1979, 7, 12), salario=Decimal('3500.00'), supervisor=f3)
f10 = Funcionario.objects.create(nome='Xuxa', sexo='F', dt_nasc=date(1970, 3, 28), salario=Decimal('13500.00'))
f11 = Funcionario.objects.create(nome='Sasha', sexo='F', dt_nasc=date(1970, 3, 28), salario=Decimal('1500.00'), supervisor=f10, depto=d3)
f12 = Funcionario.objects.create(nome='Victor', sexo='M', dt_nasc=date(1970, 3, 28), salario=Decimal('500.00'), supervisor=f2, depto=d1)
f13 = Funcionario.objects.create(nome='Humberto', sexo='M', dt_nasc=date(1970, 5, 7), salario=Decimal('1500.00'), supervisor=f2, depto=d2)
f14 = Funcionario.objects.create(nome='Doisberto', sexo='M', dt_nasc=date(1980, 7, 14), salario=Decimal('2500.00'), supervisor=f3, depto=d3)
f15 = Funcionario.objects.create(nome='Tresberta', sexo='F', dt_nasc=date(1992, 9, 1), salario=Decimal('3000.00'), supervisor=f4, depto=d3)

# ------------------------------
# Projetos
# ------------------------------
p1 = Projeto.objects.create(nome='APF', descricao='Analisador de Ponto de Função', depto=d2, responsavel=f2, data_inicio=date(2018, 2, 26), data_fim=date(2019, 6, 30))
p2 = Projeto.objects.create(nome='Monitoria', descricao='Projeto de Monitoria 2019.1', depto=d1, responsavel=f6, data_inicio=date(2019, 2, 26), data_fim=date(2019, 12, 30))
p3 = Projeto.objects.create(nome='BD', descricao='Projeto de Banco de Dados', depto=d3, responsavel=f5, data_inicio=date(2018, 2, 26), data_fim=date(2018, 6, 30))
p4 = Projeto.objects.create(nome='ES', descricao='Projeto de Engenharia de Software', depto=d1, responsavel=f1, data_inicio=date(2018, 2, 26), data_fim=date(2018, 6, 30))

# ------------------------------
# Atividades
# ------------------------------
atividades = [
    ('APF - Atividade 1', p1, '2018-02-26', '2018-06-30'),
    ('APF - Atividade 2', p1, '2018-06-26', '2018-07-30'),
    ('APF - Atividade 3', p1, '2018-08-26', '2018-09-30'),
    ('APF - Atividade 4', p1, '2018-08-26', '2018-09-30'),
    ('APF - Atividade 5', p1, '2018-09-30', '2018-10-30'),
    ('Monitoria - Atividade 1', p2, '2018-06-26', '2018-07-30'),
    ('BD - Atividade 1', p3, '2018-06-26', '2018-07-30'),
    ('BD - Atividade 2', p3, '2018-08-26', '2018-09-30'),
    ('BD - Atividade 3', p3, '2018-08-26', '2018-09-30'),
    ('ES - Atividade 1', p4, '2018-09-30', '2018-10-30'),
    ('ES - Atividade 2', p4, '2018-06-26', '2018-07-30'),
]

for desc, projeto, inicio, fim in atividades:
    Atividade.objects.create(descricao=desc, projeto=projeto, data_inicio=date.fromisoformat(inicio), data_fim=date.fromisoformat(fim))

print("Banco de dados povoado!")

