CREATE TABLE lugares (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    descripcion TEXT,
    categoria VARCHAR(50),
    latitud FLOAT,
    longitud FLOAT
);

INSERT INTO lugares (nombre, descripcion, categoria, latitud, longitud)
VALUES
('Parque Central','Centro historico','cultural',14.6349,-90.5069),
('Museo Nacional','Historia','cultural',14.6200,-90.5200),
('Gasolinera Uno','Combustible','servicio',14.6100,-90.5000),
('Lago Amatitlan','Naturaleza','natural',14.4700,-90.6200),

('Restaurante Tikal','Comida tipica','gastronomico',14.6400,-90.5100);

