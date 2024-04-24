import psycopg2

def get_connection():
    '''
    Retorna una conexión a la base de datos.

    Nota: debe ser cerrada posteriormente
    '''
    try:
        conn = psycopg2.connect(dbname="blog",
                                user="postgres", password="123456",
                                host="localhost", port="5432")

        # En Java (JDBC), por defecto las conexiones se crean con la opción
        # "autocommit = true". Esto quiere decir que cada sentencia SQL se
        # ejecuta en una transacción independiente y se acepta automáticamente.
        # En psycopg2, por defecto las conexiones se crean con la opción
        # "autocommit = false". Esto quiere decir que las sentencias SQL se
        # ejecutan en una transacción que debe ser confirmada explícitamente.
        # Por simplicidad, vamos a establecer autocommit a True para que
        # funcione como en Java.
        conn.autocommit = True

    except psycopg2.Error as e:
        # no deberíamos hacer esto, pero así vemos cuál ha sido el problema
        print("ERROR:\n{0}".format(e))

    return conn
