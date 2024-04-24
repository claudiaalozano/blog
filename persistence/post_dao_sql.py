import psycopg2
from psycopg2.extras import DictCursor

from business.entities.post import Post

from persistence import connection_manager
from persistence.post_dao import PostDao

class PostDaoSql(PostDao):

    def find_by_id(self, post_id):
        post = None

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
                     select post_id, subject, body, blog_id from post where post_id = %s
                     """)
            parameters = [post_id]

            # Para ejecutar, el primer parámetro sería la consulta, y el segundo una
            # lista con los valores de los parámetros
            cursor.execute(query, parameters)

            # si hay un resultado, lo procesamos y mapeamos a un objeto Cliente
            result = cursor.fetchone()
            if (result is not None):
                post = self.map_post(result)

            # terminado el procesado, podemos cerrar la conexión y la consulta
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            # no deberíamos hacer solo un print, pero así vemos cuál ha sido el problema
            print("ERROR:\n{0}".format(e))

        return post
        


    def find_posts(self):
        posts = []

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
                     select post_id, subject, body, blog_id from post
                     """)
            cursor.execute(query)

            # mapeamos todos los resultados
            for result in cursor:
                post = self.map_post(result)
                posts.append(post)

            # terminado el procesado, podemos cerrar la conexión y la consulta
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            # no deberíamos hacer solo un print, pero así vemos cuál ha sido el problema
            print("ERROR:\n{0}".format(e))

        return posts


    def insert_post(self, post):
        result = True

        try:
            conn = connection_manager.get_connection()
            cursor = conn.cursor()

            # preparamos la consulta y sus parámetros
            query = """ insert into post(post_id, subject, body, blog_id)
                        values (%s, %s, %s, %s) """
            parameters = (post.get_post_id(), post.get_subject(), post.get_body(), post.get_blog_id())

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


    def update_post(self, p):
        result = True

        try:
            conn = connection_manager.get_connection()
            cursor = conn.cursor()

            # preparamos la consulta y sus parámetros
            query = """ update post set post_id = %s, subject = %s, body= %s, blog_id= %s
                        where post_id = %s """
            parameters = (p.get_post_id(), p.get_subject(), p.get_body(), p.get_blog_id())

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


    def delete_post(self, p):
        result = True

        try:
            conn = connection_manager.get_connection()
            cursor = conn.cursor()

            # preparamos la consulta y sus parámetros
            query = """ delete from post where post_id = %s """
            parameters = [p.get_id()]

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


    def map_post(self, result):
        """
        Devuelve un objeto autor con los datos del resultado de la consulta
        """
        return Post(id=result['post_id'],
                      subject=result['subject'],
                      body=result['body'])