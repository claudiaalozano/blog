from persistence import daos_manager

class AuthorManager:
    """
    Gestiona las tareas acerca de autores: recibe y responde a las peticiones de
    la capa de presentación, y realiza las peticiones a la capa de persistencia
    """

    def __init__(self):
        self.author_dao = daos_manager.get_author_dao()

    def find_by_id(self, author_id):
        return self.author_dao.find_by_id(author_id)

    def find_by_username(self, username):
        # TODO: completar
        return None

    def find_authors(self):
        return self.author_dao.find_authors()

    def update_author(self, author):
        return self.author_dao.update_author(author)

    def insert_author(self, new_author):
        return self.author_dao.insert_author(new_author)

    def delete_author(self, inserted_author):
        return self.author_dao.delete_author(inserted_author)
