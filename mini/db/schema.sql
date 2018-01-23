drop table if exists users;
create table users (
  username varchar(128) not null primary key,
  password VARCHAR(128) not null
);

drop table if exists visits;
create table visits (
  username varchar(128) not null primary key,
  visits integer not null
);

insert into users (username, password) values ('admin@altavista.com','admin');
