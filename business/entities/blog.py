class Blog:

    def __init__(self, id=None, title=None, author=None, posts=[]):
        self.__id = id
        self.__title = title
        self.__author = author
        self.__posts = posts

    def __str__(self):
        result =  (f"Blog {{\n"
                   f"\tID: {self.__id}\n"
                   f"\tTitle: {self.__title}")

        if self.__author is not None:
            result += f"\n\tAuthor: {self.__author}"

        if (len(self.__posts) > 0):
            result += f"\n\tPosts: ["
            for p in self.__posts:
                result += f"\n\t\t{p}"
            result += f"\n\t]"

        result += "\n}"

        return result

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_posts(self):
        return self.__posts

    def set_posts(self, posts):
        self.__posts = posts
