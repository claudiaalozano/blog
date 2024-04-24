import psycopg2
from psycopg2.extras import DictCursor

from business.entities.blog import Blog

from persistence import connection_manager
from persistence.blog_dao import BlogDao
from persistence.author_dao_sql import AuthorDaoSql
from persistence.post_dao_sql import PostDaoSql

class BlogDaoSql(BlogDao):

        def find_by_id(self, blog_id):
            blog = None

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
                        select blog_id, title from blog where blog_id = %s
                        """)
                parameters = [blog_id]

                # Para ejecutar, el primer parámetro sería la consulta, y el segundo una
                # lista con los valores de los parámetros
                cursor.execute(query, parameters)

                # si hay un resultado, lo procesamos y mapeamos a un objeto Cliente
                result = cursor.fetchone()
                if (result is not None):
                    blog = self.map_blog(result)

                # terminado el procesado, podemos cerrar la conexión y la consulta
                cursor.close()
                conn.close()
            except psycopg2.Error as e:
                # no deberíamos hacer solo un print, pero así vemos cuál ha sido el problema
                print("ERROR:\n{0}".format(e))

            return blog


        def find_by_id_with_author(self, blog_id):
            blog = None

            try:
                conn = connection_manager.get_connection()

                # creamos un cursor para ejecutar la consulta. La parte de
                # "cursor_factory=DictCursor" es para que los resultados se
                # devuelvan como diccionarios, en lugar de tuplas a las que
                # tenemos que acceder con índices numéricos
                cursor = conn.cursor(cursor_factory=DictCursor)

                # en esta consulta hay un join, que en otros casos hemos
                # realizado de tipo left (por si un blog no tuviera un autor).
                # No obstante, en esta BD todos los blogs tienen siempre un
                # autor (es un campo not null)

                query = ("""
                         select b.blog_id, b.title,
                                a.author_id, a.username, a.email
                         from blog b
                         inner join author a on a.author_id = b.author_id
                         where b.blog_id = %s
                         """)
                parametros = [blog_id]

                # Para ejecutar, el primer parámetro sería la consulta, y el segundo una
                # lista con los valores de los parámetros
                cursor.execute(query, parametros)

                # si hay un resultado, lo procesamos y mapeamos a un objeto Cliente
                result = cursor.fetchone()
                if (result is not None):
                    blog = self.map_blog(result)

                    # procesamos el autor con su propio dao
                    author_dao = AuthorDaoSql()
                    author = author_dao.map_author(result)
                    blog.set_author(author)

                # terminado el procesado, podemos cerrar la conexión y la consulta
                cursor.close()
                conn.close()
            except psycopg2.Error as e:
                # no deberíamos hacer solo un print, pero así vemos cuál ha sido el problema
                print("ERROR:\n{0}".format(e))

            return blog


        def map_blog(self, result):
             return Blog(id=result['blog_id'],
                         title=result['title'])
