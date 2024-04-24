import psycopg2
from psycopg2.extras import DictCursor

from business.entities.post import Post

from persistence import connection_manager
from persistence.post_dao import PostDao

class PostDaoSql(PostDao):

    def find_by_id(self, post_id):
        # TODO: completar
        return None


    def find_posts(self):
        # TODO: completar
        return None


    def insert_post(self, post):
        # TODO: completar
        return None


    def update_post(self, p):
        # TODO: completar
        return None


    def delete_post(self, p):
        # TODO: completar
        return None
