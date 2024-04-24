from abc import ABC, abstractmethod

class AuthorDao(ABC):

    @abstractmethod
    def find_by_id(self, author_id):
        pass

    @abstractmethod
    def find_by_username(self, username):
        pass

    @abstractmethod
    def find_authors(self):
        pass

    @abstractmethod
    def insert_author(self, author):
        pass

    @abstractmethod
    def update_author(self, author):
        pass

    @abstractmethod
    def delete_author(self, author):
        pass
