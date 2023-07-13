create table usuario 
(
	idUsuario int not null primary key not null auto_increment,
    user varchar(50) not null,
    password varchar (50) not null
);
alter table usuario add column tipoUsuario int not null;

insert into usuario(user, password) values("admin", "admin");
insert into usuario(user, password) values("user", "user");
Select * from usuario;
update usuario set tipoUsuario=1 where idUsuario=1;
update usuario set tipoUsuario=2 where idUsuario=2;




/* Optica Jimmy */
CREATE DATABASE optica_jimmy;

USE optica_jimmy;

CREATE TABLE lentes (
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(255) NOT NULL,
  tamanio VARCHAR(255) NOT NULL,
  presentacion VARCHAR(255) NOT NULL,
  precio DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE armazones (
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(255) NOT NULL,
  precio DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE ventas (
  id INT NOT NULL AUTO_INCREMENT,
  fecha DATE NOT NULL,
  lente_id INT NOT NULL,
  armazón_id INT NOT NULL,
  cantidad INT NOT NULL,
  total DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (id)
);

ALTER TABLE ventas
  ADD FOREIGN KEY (lente_id)
  REFERENCES lentes (id);

ALTER TABLE ventas
  ADD FOREIGN KEY (armazón_id)
  REFERENCES armazones (id);