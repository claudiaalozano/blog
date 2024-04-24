create table author (
    author_id int primary key,
    username varchar(40) not null unique,
    email varchar(40) not null
);

create table blog (
    blog_id int primary key,
    title varchar(100) not null,
    author_id int not null references author(author_id)
);

create table post (
    post_id int primary key,
    subject varchar(100) not null,
    body varchar(1000) not null,
    blog_id int references blog(blog_id)
);
