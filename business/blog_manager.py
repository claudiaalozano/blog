from persistence import daos_manager

class BlogManager:
    """
    Gestiona las tareas acerca de blogs: recibe y responde a las peticiones de
    la capa de presentación, y realiza las peticiones a la capa de persistencia
    """

    def __init__(self):
        self.blog_dao = daos_manager.get_blog_dao()

    def find_by_id(self, id):
        return self.blog_dao.find_by_id(id)

    def find_by_id_with_author(self, id):
        return self.blog_dao.find_by_id_with_author(id)

    def find_by_id_with_author_and_posts(self, id):
        # TODO: completar
        return None
