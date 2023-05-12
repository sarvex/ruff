# single-line failures
query1 = f"SELECT {var} FROM table"
query2 = f"SELECT var FROM {table}"
query3 = f"SELECT {val} FROM {table}"
query4 = f"SELECT {var} FROM table;"
query5 = f"SELECT * FROM table WHERE var = {var}"

query6 = f"DELETE FROM table WHERE var = {var}"
query7 = f"DELETE FROM table WHERE VAR = {var}"
query8 = f"DELETE FROM {table}WHERE var = {var}"
query9 = f"DELETE FROM table WHERE var = {var}"
query10 = f"DELETE FROM table WHERE var = {var}"

query11 = f"INSERT INTO table VALUES ({var})"
query12 = f"INSERT INTO TABLE VALUES ({var})"
query13 = f"INSERT INTO {table} VALUES ({var})"
query14 = f"INSERT INTO {table} VALUES var = {var}"

query15 = f"UPDATE {table} SET var = {var}"
query16 = f"UPDATE {table} SET var = {var}"
query17 = f"UPDATE {table} SET var = {var}"
query18 = f"UPDATE {table} SET var = {var}"

query19 = f"select {var} from table"
query20 = f"select var from {table}"
query21 = f"select {val} from {table}"
query22 = f"select {var} from table;"
query23 = f"select * from table where var = {var}"

query24 = f"delete from table where var = {var}"
query25 = f"delete from table where var = {var}"
query26 = f"delete from {table}where var = {var}"
query27 = f"delete from table where var = {var}"
query28 = f"delete from table where var = {var}"

query29 = f"insert into table values ({var})"
query30 = f"insert into table values ({var})"
query31 = f"insert into {table} values ({var})"
query32 = f"insert into {table} values var = {var}"

query33 = f"update {table} set var = {var}"
query34 = f"update {table} set var = {var}"
query35 = f"update {table} set var = {var}"
query36 = f"update {table} set var = {var}"

# multi-line failures
def query37():
    return """
    SELECT *
    FROM table
    WHERE var = %s
    """ % var

def query38():
    return """
    SELECT *
    FROM TABLE
    WHERE var =
    """ + var

def query39():
    return """
    SELECT *
    FROM table
    WHERE var = {}
    """.format(var)

def query40():
    return f"""
    SELECT *
    FROM table
    WHERE var = {var}
    """

def query41():
    return (
        "SELECT *"
        "FROM table"
        f"WHERE var = {var}"
    )

# # cursor-wrapped failures
query42 = cursor.execute(f"SELECT * FROM table WHERE var = {var}")
query43 = cursor.execute(f"SELECT * FROM table WHERE var = {var}")
query44 = cursor.execute(f"SELECT * FROM table WHERE var = {var}")
query45 = cursor.executemany(f"SELECT * FROM table WHERE var = {var}", [])

# # pass
query = "SELECT * FROM table WHERE id = 1"
query = "DELETE FROM table WHERE id = 1"
query = "INSERT INTO table VALUES (1)"
query = "UPDATE table SET id = 1"
cursor.execute('SELECT * FROM table WHERE id = %s', var)
cursor.execute('SELECT * FROM table WHERE id = 1')
cursor.executemany('SELECT * FROM table WHERE id = %s', [var, var2])
