from persistence import daos_manager

class PostManager:
    """
    Gestiona las tareas acerca de posts: recibe y responde a las peticiones de
    la capa de presentación, y realiza las peticiones a la capa de persistencia
    """

    def __init__(self):
        self.post_dao = daos_manager.get_post_dao()

    def find_by_id(self, post_id):
        return self.post_dao.find_by_id(post_id)

    def find_posts(self):
        return self.find_posts_dao()

    def insert_post(self, post):
        return self.post_dao.insert_post(post)
    
    def update_post(self, post):
        return self.post_dao.update_post(post)

    def delete_post(self, post):
        return self.post_dao.delete_post(post)
