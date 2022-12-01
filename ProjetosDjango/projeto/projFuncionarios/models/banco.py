import sqlite3

conexao = sqlite3.connect('projeto\\projFuncionarios\\models\\bancoDeDados.db')
cursor = conexao.cursor()

sql = """
    CREATE TABLE funcionarios (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        cpf TEXT NOT NULL,
        service_time INTEGER NOT NULL,
        remuneration INTEGER NOT NULL
    )
"""

cursor.execute(sql)
conexao.commit()
conexao.close()
