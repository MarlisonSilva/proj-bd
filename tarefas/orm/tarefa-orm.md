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
