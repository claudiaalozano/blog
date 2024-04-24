"""
Esta clase nos permite obtener los objetos Dao adecuados para acceder a los
sistemas de persistencia de nuestra aplicación.

Básicamente, "inyecta" o enlaza las implementaciones con las interfaces Dao correspondientes,
de forma que no tengamos que instanciar tipos concretos en el código de
nuestra aplicación, y éstos puedan ser cambiados limpiamente en esta clase.

Este es un concepto avanzado en el que se ahonda más profundamente en futuros
cursos, sobre todo en la Mención de Ingeniería del Software. Para leer más
acerca de por qué se hace esto, se pueden consultar estos enlaces acerca de
inyección de dependencias (Dependency Injection)

- Cómic: https://cdn-media-1.freecodecamp.org/images/1*TF-VdAgPfcD497kAW77Ukg.png
- Artículo completo: https://www.freecodecamp.org/news/a-quick-intro-to-dependency-injection-what-it-is-and-when-to-use-it-7578c84fa88f/
- Más técnico: https://en.wikipedia.org/wiki/Dependency_injection
"""

from persistence.author_dao_sql import AuthorDaoSql
from persistence.blog_dao_sql import BlogDaoSql
from persistence.post_dao_sql import PostDaoSql

def get_author_dao():
    return AuthorDaoSql()

def get_blog_dao():
    return BlogDaoSql()

def get_post_dao():
    return PostDaoSql()
