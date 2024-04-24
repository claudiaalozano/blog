class Author:

    def __init__(self, id=None, username=None, email=None):
        self.__id = id
        self.__username = username
        self.__email = email


    def __str__(self):
        return (f"Author {{ "
                f"ID: {self.__id}; "
                f"username: {self.__username}; "
                f"email: {self.__email} "
                f"}}")

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email
