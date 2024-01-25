create database netflix;

create table usuario (
id int auto_increment,
nome varchar (30) not null,
cpf int not null,
fone int not null,
email varchar (30) not null,
senha varchar (20) not null,
endereço varchar (30) not null,
cartão varchar (30) not null,
primary key (id)
);

create database mensalidade;

create table mensalidade (
mes int not null,
valorpago int not null,
datapago int null
);

create database video; 

create table video (
tipo varchar (20) not null,
produtora varchar (30) not null,
duracao float not null,
ano int not null,
titulo varchar (1) not null,
episodio int not null,
temporada int not null
);

create database ator;

create table ator (
localdenascimento int not null,
datadenascimento int not null,
nome varchar (1) not null
);

