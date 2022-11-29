import sqlite3

conexao = sqlite3.connect('projeto\\projFuncionarios\\bancoDeDados.db')
cursor = conexao.cursor()

# CREATE
def db_insert(name, surname, cpf, service_time, remuneration):
    return f"""
        INSERT INTO funcionarios ( name, surname, cpf, service_time, remuneration )
            VALUES ('{name}', '{surname}', '{cpf}', {service_time}, {remuneration})
    """

# READ
def db_select(data, field):
    return f"""
        SELECT id, name, surname, cpf, service_time, remuneration
            FROM funcionarios WHERE {field} = {data}
    """

# UPDATE
def db_udpate(name, surname):
    return f"""
        UPDATE funcionarios SET nome = '{name}'
            WHERE surname = '{surname}'
    """

# DELETE
def db_delete(data, field):
    return f"""
        DELETE FROM funcionarios WHERE {field} = '{data}'
    """

cursor.execute(db_delete('2', 'id'))
conexao.commit()
conexao.close()
