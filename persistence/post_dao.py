from abc import ABC, abstractmethod

class PostDao(ABC):

    @abstractmethod
    def find_by_id(self, post_id):
        pass

    @abstractmethod
    def find_posts(self):
        pass

    @abstractmethod
    def insert_post(self, p):
        pass

    @abstractmethod
    def update_post(self, p):
        pass

    @abstractmethod
    def delete_post(self, p):
        pass
