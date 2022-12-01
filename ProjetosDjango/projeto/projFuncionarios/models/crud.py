import sqlite3

def commit_close(function):
    def decorator(*args):
        # Connect and instaciate database cursor
        conexao = sqlite3.connect('projeto\\projFuncionarios\\models\\bancoDeDados.db')
        cursor = conexao.cursor()

        sql = function(*args)
        cursor.execute(sql)

        conexao.commit()
        conexao.close()

    return decorator

# CREATE
@commit_close
def db_insert(name, surname, cpf, service_time, remuneration):
    return f"""
        INSERT INTO funcionarios ( name, surname, cpf, service_time, remuneration )
            VALUES ('{name}', '{surname}', '{cpf}', {service_time}, {remuneration})
    """

# READ
def db_select(data, field):

    conexao = sqlite3.connect('projeto\\projFuncionarios\\models\\bancoDeDados.db')
    cursor = conexao.cursor()

    sql = f"""
        SELECT id, name, surname, cpf, service_time, remuneration
            FROM funcionarios WHERE {field} = '{data}'
    """

    cursor.execute(sql)
    data = cursor.fetchall()
    conexao.close()
    
    return data

# UPDATE
@commit_close
def db_udpate(changeField, newValue, referenceField, refFieldValue):
    return f"""
        UPDATE funcionarios SET {changeField} = '{newValue}'
            WHERE {referenceField} = '{refFieldValue}'
    """

# DELETE
@commit_close
def db_delete(data, field):
    return f"""
        DELETE FROM funcionarios WHERE {field} = '{data}'
    """

