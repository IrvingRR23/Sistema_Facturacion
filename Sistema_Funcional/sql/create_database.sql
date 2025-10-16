CREATE DATABASE IF NOT EXISTS restaurante;
USE restaurante;

CREATE TABLE IF NOT EXISTS usuarios(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    usuario VARCHAR(50) UNIQUE,
    password VARCHAR(100),
    rol ENUM('admin','empleado') DEFAULT 'empleado'
);

CREATE TABLE IF NOT EXISTS productos (
	id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    categoria ENUM('Comida','Bebida','Postre'),
    precio DECIMAL(10,2)
);

CREATE TABLE IF NOT EXISTS ventas(
	id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATETIME,
    total DECIMAL(10,2),
    cajero VARCHAR(50)
);