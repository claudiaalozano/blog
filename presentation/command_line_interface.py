"""
Permite leer y escribir información por consola de texto
"""

from business.entities.author import Author
from business.entities.post import Post

def show_message(message):
    print(message)

def new_line():
    show_message("")

def show_element(element):
    show_message(element)
    new_line()

def show_separator():
    show_message("*************************************************")

def read_option(message):
    return read_int(message)

def read_int(message):
    res = -1
    correct_input = False

    while not correct_input:
        try:
            res = int(input(message))
            correct_input = True
        except ValueError:
            show_message("Invalid input. Please enter a number.")
            new_line()

    return res

def read_string(message):
    return input(message)

def read_author():
    author = Author()
    author.set_id(read_int("Enter the author's id: "))
    author.set_username(read_string("Enter the author's username: "))
    author.set_email(read_string("Enter the author's email: "))
    return author

def read_post():
    post = Post()
    post.set_id(read_int("Enter the post's id: "))
    post.set_subject(read_string("Enter the post's subject: "))
    post.set_body(read_string("Enter the post's body: "))
    return post
