from persistence import daos_manager

class PostManager:
    """
    Gestiona las tareas acerca de posts: recibe y responde a las peticiones de
    la capa de presentación, y realiza las peticiones a la capa de persistencia
    """

    def __init__(self):
        self.post_dao = daos_manager.get_post_dao()

    def find_by_id(self, post_id):
        # TODO: completar
        return None

    def find_posts(self):
        # TODO: completar
        return None

    def insert_post(self, post):
        # TODO: completar
        return None

    def update_post(self, post):
        # TODO: completar
        return None

    def delete_post(self, post):
        # TODO: completar
        return None
