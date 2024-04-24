delete from post;
delete from blog;
delete from author;

insert into author
    (author_id, username, email)
values
    (1, 'alice', 'alice@amail.com'),
    (2, 'bob', 'bob@bmail.com'),
    (3, 'charlie', 'charlie@cmail.com');


insert into blog
    (blog_id, title, author_id)
values
    (1, 'Alice in Wonderland', 1),
    (2, 'SpongeBob SquarePants', 2),
    (3, 'Charlie and his sugar-free factory', 3);


insert into post
    (post_id, subject, body, blog_id)
VALUES
    (1, 'Follow the white rabbit', 'Knock knock, John Wick', 1),
    (2, 'Es Patricio el mejor personaje o no', 'Calamardo en un claro segundo puesto', 2),
    (3, 'Is Agent Smith in Cyberpunk?', 'Or in Rivendel?', 1);


/* Consultas auxiliares */
select * from author;
select * from blog;
select * from post;
