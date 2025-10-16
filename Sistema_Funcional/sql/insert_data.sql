USE restaurante;

INSERT INTO usuarios (nombre, usuario, password, rol)
VALUES ('Administrador General', 'admin', '1234', 'admin')
ON DUPLICATE KEY UPDATE usuario = usuario;

INSERT INTO productos (nombre, categoria, precio) VALUES
('Pizza', 'Comida', 120.00),
('Hamburguesa', 'Comida', 85.00),
('Hot Dog', 'Comida', 25.00),
('Tacos', 'Comida', 70.00),
('Ensalada', 'Comida', 45.00),
('Pasta', 'Comida', 75.00),
('Sopa', 'Comida', 35.00),
('Sandwich', 'Comida', 30.00);


INSERT INTO productos (nombre, categoria, precio) VALUES
('Agua', 'Bebida', 20.00),
('Refresco', 'Bebida', 25.00),
('Cerveza', 'Bebida', 45.00),
('Vino', 'Bebida', 120.00),
('Café', 'Bebida', 30.00),
('Té', 'Bebida', 25.00),
('Jugo', 'Bebida', 30.00),
('Tequila', 'Bebida', 80.00);

INSERT INTO productos (nombre, categoria, precio) VALUES
('Pastel', 'Postre', 55.00),
('Helado', 'Postre', 35.00),
('Gelatina', 'Postre', 25.00),
('Flan', 'Postre', 30.00),
('Pay de Queso', 'Postre', 48.00),
('Fruta Picada', 'Postre', 32.00),
('Brownie', 'Postre', 40.00),
('Cupcake', 'Postre', 35.00);
