import psycopg2
from psycopg2.extras import DictCursor

from business.entities.author import Author

from persistence.author_dao import AuthorDao
from persistence import connection_manager

class AuthorDaoSql(AuthorDao):

    def find_by_id(self, author_id):
        author = None

        try:
            conn = connection_manager.get_connection()

            # creamos un cursor para ejecutar la consulta. La parte de
            # "cursor_factory=DictCursor" es para que los resultados se devuelvan
            # como diccionarios, en lugar de tuplas a las que tenemos que acceder
            # con índices numéricos
            cursor = conn.cursor(cursor_factory=DictCursor)

            # En python, los parámetros se pasan directamente en el comando de
            # ejecución de una consulta, en lugar de "preparar" la consulta mediante
            # un PreparedStatement como en Java. También, para indicar los
            # parámetros, se utiliza % en lugar de ?, indicando el tipo

            # https://www.psycopg.org/docs/usage.html#query-parameters

            query = ("""
                     select author_id, username, email from author where author_id = %s
                     """)
            parameters = [author_id]

            # Para ejecutar, el primer parámetro sería la consulta, y el segundo una
            # lista con los valores de los parámetros
            cursor.execute(query, parameters)

            # si hay un resultado, lo procesamos y mapeamos a un objeto Cliente
            result = cursor.fetchone()
            if (result is not None):
                author = self.map_author(result)

            # terminado el procesado, podemos cerrar la conexión y la consulta
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            # no deberíamos hacer solo un print, pero así vemos cuál ha sido el problema
            print("ERROR:\n{0}".format(e))

        return author


    def find_by_username(self, username):
        # TODO: completar
        return None


    def find_authors(self):
        authors = []

        try:
            conn = connection_manager.get_connection()

            # creamos un cursor para ejecutar la consulta. La parte de
            # "cursor_factory=DictCursor" es para que los resultados se devuelvan
            # como diccionarios, en lugar de tuplas a las que tenemos que acceder
            # con índices numéricos
            cursor = conn.cursor(cursor_factory=DictCursor)

            # En python, los parámetros se pasan directamente en el comando de
            # ejecución de una consulta, en lugar de "preparar" la consulta mediante
            # un PreparedStatement como en Java. También, para indicar los
            # parámetros, se utiliza % en lugar de ?, indicando el tipo

            # https://www.psycopg.org/docs/usage.html#query-parameters

            # consulta simple, sin parámetros
            query = ("""
                     select author_id, username, email from author
                     """)
            cursor.execute(query)

            # mapeamos todos los resultados
            for result in cursor:
                author = self.map_author(result)
                authors.append(author)

            # terminado el procesado, podemos cerrar la conexión y la consulta
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            # no deberíamos hacer solo un print, pero así vemos cuál ha sido el problema
            print("ERROR:\n{0}".format(e))

        return authors


    def insert_author(self, author):
        result = True

        try:
            conn = connection_manager.get_connection()
            cursor = conn.cursor()

            # preparamos la consulta y sus parámetros
            query = """ insert into author(author_id, username, email)
                        values (%s, %s, %s) """
            parameters = (author.get_id(), author.get_username(), author.get_email())

            # ejecutamos la consulta
            cursor.execute(query, parameters)

            # si no se ha insertado una fila, algo ha ido mal
            if cursor.rowcount != 1:
                result = False

            # haya salido bien o mal la inserción, siempre debemos cerrar los recursos
            cursor.close()
            conn.close()

        except psycopg2.Error as e:
            # no deberíamos hacer solo un print, pero así vemos cuál ha sido el problema
            print("ERROR:\n{0}".format(e))

        return result


    def update_author(self, author):
        result = True

        try:
            conn = connection_manager.get_connection()
            cursor = conn.cursor()

            # preparamos la consulta y sus parámetros
            query = """ update author set username = %s, email = %s
                        where author_id = %s """
            parameters = (author.get_username(), author.get_email(), author.get_id())

            # ejecutamos la consulta
            cursor.execute(query, parameters)

            # si no se ha insertado una fila, algo ha ido mal
            if cursor.rowcount != 1:
                result = False

            # haya salido bien o mal la inserción, siempre debemos cerrar los recursos
            cursor.close()
            conn.close()

        except psycopg2.Error as e:
            # no deberíamos hacer solo un print, pero así vemos cuál ha sido el problema
            print("ERROR:\n{0}".format(e))

        return result


    def delete_author(self, author):
        result = True

        try:
            conn = connection_manager.get_connection()
            cursor = conn.cursor()

            # preparamos la consulta y sus parámetros
            query = """ delete from author where author_id = %s """
            parameters = [author.get_id()]

            # ejecutamos la consulta
            cursor.execute(query, parameters)

            # si no se ha insertado una fila, algo ha ido mal
            if cursor.rowcount != 1:
                result = False

            # haya salido bien o mal la inserción, siempre debemos cerrar los recursos
            cursor.close()
            conn.close()

        except psycopg2.Error as e:
            # no deberíamos hacer solo un print, pero así vemos cuál ha sido el problema
            print("ERROR:\n{0}".format(e))

        return result


    def map_author(self, result):
        """
        Devuelve un objeto autor con los datos del resultado de la consulta
        """
        return Author(id=result['author_id'],
                      username=result['username'],
                      email=result['email'])
