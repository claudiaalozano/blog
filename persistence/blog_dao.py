from abc import ABC, abstractmethod

class BlogDao(ABC):

    @abstractmethod
    def find_by_id(self, blog_id):
        pass

    @abstractmethod
    def find_by_id_with_author(self, blog_id):
        pass
