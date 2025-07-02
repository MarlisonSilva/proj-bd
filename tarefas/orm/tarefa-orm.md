# ODBC em Python

ODBC (Open Database Connectivity) é uma interface padrão que permite que aplicações acessem diferentes sistemas gerenciadores de banco de dados (SGBDs) usando comandos SQL. Em Python, o acesso via ODBC pode ser feito com pacotes como pyodbc. Esse pacote permite conectar a bancos como PostgreSQL, SQL Server, entre outros, utilizando drivers compatíveis. No caso do PostgreSQL, o driver mais comum é o psqlODBC. Apesar disso, em projetos Python modernos é mais comum usar bibliotecas específicas como psycopg2 para PostgreSQL.

Exemplo de uso:

``` python
import pyodbc

conn = pyodbc.connect(
    "DRIVER={PostgreSQL Unicode};"
    "SERVER=localhost;"
    "PORT=5432;"
    "DATABASE=AtividadesBD;"
    "UID=usuario;"
    "PWD=senha;"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM projeto;")
for row in cursor.fetchall():
    print(row)

conn.close()
```

# ORM em Python com Django

ORM (Object-Relational Mapping) é uma técnica que permite interagir com o banco de dados usando objetos da linguagem de programação, sem escrever SQL diretamente. O Django possui um ORM robusto e integrado que facilita a definição de modelos (tabelas), criação de consultas e manipulação de dados. Com ele, é possível criar e gerenciar o banco de dados usando classes Python, o que reduz erros e aumenta a produtividade. O ORM do Django suporta múltiplos SGBDs, incluindo PostgreSQL, e permite realizar operações como inserção, atualização e busca de dados de forma simples e elegante.

### Utilização No Django

No Django,a definição é feita na classe de modelos (models) como classes Python que representam tabelas no banco de dados. Cada atributo da classe representa uma coluna da tabela.

`````
from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=150)
    sexo = models.CharField(max_length=1)
    dt_nasc = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    supervisor = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    depto = models.ForeignKey('Departamento', null=True, blank=True, on_delete=models.SET_NULL)

class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10, unique=True)
    descricao = models.TextField()
    gerente = models.ForeignKey(Funcionario, null=True, blank=True, on_delete=models.SET_NULL)

````
`````

# Criar o Container do BD

docker run --name postgres_db \
 -e POSTGRES_USER=usuario \
 -e POSTGRES_PASSWORD=senha123 \
 -e POSTGRES_DB=AtividadesBD \
 -v postgres_data:/var/lib/postgresql/data \
 -p 5432:5432 \
 -d postgres:latest

user_name:usuario
password:senha123
nome_do_banco:AtividadesBD
funcionando:localhost
porta:5432

## Criar Container Pgadmin

docker run --name pgadmin \
 -e PGADMIN_DEFAULT_EMAIL=admin@admin.com \
 -e PGADMIN_DEFAULT_PASSWORD=admin123 \
 -p 80:80 \
 --link postgres_db:db \
 -d dpage/pgadmin4

email:admin@admin.com
password:admin123
porta:localhot:80

## Utilização PG Admin

Entre em **Localhost:80** e insira o login

email:admin@admin.com

password:admin123

porta:localhot:80

# Esquema do Banco De Dados

[Banco_De_Dados](/tarefa_bd/tarefas/orm/esquema_bd.sql)

[Querys](/tarefa_bd/tarefas/orm/querys.sql)

## Driver Para Instalar O postgress no Django

**pip install psycopg2-binary**

## Arquivo Models

[Models](./django/orm_django/app_django/models.py)

### Comandos para executar após criar o models

```
python manage.py makemigrations
python manage.py migrate
```

## Script De Povoamento Do banco

[Povoamento](./django/orm_django/app_django/management/commands/seed.py)

### Comando para realizar o povoamento

**python manage.py seed**

## Rodar Final

Agora rode o django **Python manage.py runserver**

# Teste

E teste as querys nas telas
