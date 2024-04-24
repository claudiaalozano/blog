from presentation import command_line_interface as cli

from business.author_manager import AuthorManager
from business.blog_manager import BlogManager
from business.post_manager import PostManager

def run():
    """
    Crea y gestiona un menú de operaciones por consola de texto
    """

    cli.show_message("Enter a number to select the operations to run:")
    cli.show_message("1: Author operations (complete)")
    cli.show_message("2: Blog operations (complete)")
    cli.show_message("3: Find author by username (exercise)")
    cli.show_message("4: Post operations (exercise)")
    cli.show_message("5: Find blog with author and posts (exercise)")
    cli.show_separator()

    option = cli.read_option("Enter a number [1-5]: ")
    print(option)

    if option == 1:
        author_operations()
    elif option == 2:
        blog_operations()
    elif option == 3:
        find_author_by_username()
    elif option == 4:
        post_operations()
    elif option == 5:
        find_blog_with_author_and_posts()
    else:
        cli.show_message("Invalid option. Next time, enter a number 1 to 5. Exiting.")

    print("Done.")

def author_operations():
    author_manager = AuthorManager()

    cli.new_line()
    cli.show_message("Show all the authors in the database: ")
    cli.new_line()

    authors = author_manager.find_authors()
    for author in authors:
        cli.show_element(author)

    cli.show_separator()

    authorId = cli.read_int("Enter the id of an author: ")
    author = author_manager.find_by_id(authorId)

    if author is None:
        cli.show_message("Author not found")
        return

    cli.show_element(author)
    cli.show_separator()

    new_username = cli.read_string("Enter a new username for the author: ")
    old_username = author.get_username() # we save it to restore it later

    author.set_username(new_username)
    result = author_manager.update_author(author)
    if not result:
        cli.show_message("Update error. Exiting.")
        return

    cli.show_element(author)

    cli.show_message("You can check the database now to see the updated username")
    cli.read_string("Continue? (write yes, username change will be reverted): ")

    # This reverts changes to allow re-running the main program later
    author.set_username(old_username)
    result = author_manager.update_author(author)
    if not result:
        cli.show_message("Revert error. Exiting.")
        return

    cli.show_separator()

    cli.show_message("Now we ask for the details to insert a new author")

    new_author = cli.read_author()
    cli.show_element(new_author)
    result = author_manager.insert_author(new_author)
    if not result:
        cli.show_message("Insertion error. Exiting.")
        return

    new_author_id = new_author.get_id()

    cli.show_message("We delete our local copy (will be garbage collected)")
    new_author = None

    cli.show_message("Now we read the inserted author")
    inserted_author = author_manager.find_by_id(new_author_id)

    cli.show_element(inserted_author)

    cli.show_separator()

    cli.show_message("Finally, we delete the inserted author")
    cli.read_string("Write yes to continue with the deletion: ")

    result = author_manager.delete_author(inserted_author)
    if not result:
        cli.show_message("Deletion error. Exiting.")
        return
    inserted_author = None

    cli.show_message("We check if it has been properly deleted (None in that case)\n")
    deleted_author = author_manager.find_by_id(new_author_id)
    cli.show_element(deleted_author)

def blog_operations():
    blog_manager = BlogManager()

    blog_id = cli.read_int("Enter the id of a blog to find: ")
    cli.show_separator()

    blog = blog_manager.find_by_id(blog_id)
    cli.show_message("Blog loaded (only basic attributes):")
    cli.show_element(blog)

    cli.show_separator()

    blog = blog_manager.find_by_id_with_author(blog_id)
    cli.show_message("Blog loaded (with author):")
    cli.show_element(blog)

def find_author_by_username():
    author_manager = AuthorManager()

    username = cli.read_string("Enter the username of an author: ")
    author = author_manager.find_by_username(username)

    if author is None:
        cli.show_message("Author not found")
    else:
        cli.show_element(author)

def post_operations():
    cli.show_separator()

    cli.show_message("Enter a number to select the post operation:")
    cli.show_message("1: Find post by id")
    cli.show_message("2: Insert new post")
    cli.show_message("3: Find post and update subject")
    cli.show_message("4: List posts and delete one of them")
    cli.show_separator()

    option = cli.read_option("Enter a number [1-5]: ")

    if option == 1:
        find_post()
    elif option == 2:
        insert_post()
    elif option == 3:
        find_post_and_update_subject()
    elif option == 4:
        list_posts_and_delete_one()
    else:
        cli.show_message("Invalid option. Next time, enter a number 1 to 4. Exiting.")

def find_post():
    post_manager = PostManager()

    post_id = cli.read_int("Enter the id of a post: ")

    cli.new_line()

    post = post_manager.find_by_id(post_id)
    if post is None:
        cli.show_message("Post not found")
        return

    cli.show_element(post)

def insert_post():
    post_manager = PostManager()

    post = cli.read_post()
    result = post_manager.insert_post(post)
    if not result:
        cli.show_message("Insertion error. Exiting.")
        return

def find_post_and_update_subject():
    post_manager = PostManager()

    post_id = cli.read_int("Enter the id of a post: ")

    post = post_manager.find_by_id(post_id)
    if post is None:
        cli.show_message("Post not found")
        return

    cli.show_element(post)

    cli.show_separator()

    new_subject = cli.read_string("Enter a new subject for the post: ")
    post.set_subject(new_subject)
    result = post_manager.update_post(post)
    if not result:
        cli.show_message("Update error. Exiting.")
        return

    cli.show_element(post)

def list_posts_and_delete_one():
    post_manager = PostManager()

    cli.show_message("Posts:")
    cli.new_line()

    posts = post_manager.find_posts()
    for post in posts:
        cli.show_element(post)

    post_id = cli.read_int("Enter the id of the post to delete: ")
    post = find_post_in_list(post_id, posts)
    if post is None:
        cli.show_message("That is not a valid post id. Exiting.")
        return

    cli.show_element(post)

    cli.read_string("This post will be deleted. Press enter to continue.")

    cli.show_message("Deleting...")
    result = post_manager.delete_post(post)
    if not result:
        cli.show_message("Deletion error. Exiting.")
        return

def find_post_in_list(post_id, posts):
    for post in posts:
        if post.get_id() == post_id:
            return post
    return None

def find_blog_with_author_and_posts():

    blog_manager = BlogManager()

    blog_id = cli.read_int("Enter the id of a blog to find:")
    cli.show_separator()

    blog = blog_manager.find_by_id_with_author_and_posts(blog_id)
    cli.show_message("Blog loaded (with author and posts):")
    cli.show_element(blog)
