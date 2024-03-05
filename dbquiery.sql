create database socialnetwork;

use socialnetwork;
show tables;

select * from mainapp_posts_liked_by;
select * from mainapp_posts;
select * from auth_user;
select * from mainapp_userprofile;
delete from mainapp_posts where id=2;

alter table mainapp_userprofile add column profile_picture LONGBLOB NULL
