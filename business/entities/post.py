class Post:

    def __init__(self, id=None, subject=None, body=None):
        self.__id = id
        self.__subject = subject
        self.__body = body

    def __str__(self):
        return (f"Post {{ ID: {self.__id}; "
                f"Subject: {self.__subject}; Body: {self.__body} }}")

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_subject(self):
        return self.__subject

    def set_subject(self, subject):
        self.__subject = subject

    def get_body(self):
        return self.__body

    def set_body(self, body):
        self.__body = body
