CREATE DATABASE actividades_deportivas;

USE actividades_deportivas;

CREATE TABLE estudiante (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    documento VARCHAR(20) UNIQUE,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    carrera VARCHAR(100),
    facultad VARCHAR(100)
);

CREATE TABLE disciplina (
    id_disciplina INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50)
);

CREATE TABLE espacio (
    id_espacio INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    ubicacion VARCHAR(100),
    capacidad INT
);

CREATE TABLE actividad (
    id_actividad INT AUTO_INCREMENT PRIMARY KEY,
    nombre_actividad VARCHAR(100),
    id_disciplina INT,
    id_espacio INT,
    cupo_max INT,
    dia VARCHAR(20),
    horario TIME,
    estado VARCHAR(20),
    FOREIGN KEY (id_disciplina) REFERENCES disciplina(id_disciplina),
    FOREIGN KEY (id_espacio) REFERENCES espacio(id_espacio)
);

CREATE TABLE inscripcion (
    id_inscripcion INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT,
    id_actividad INT,
    estado_inscripcion VARCHAR(20),
    fecha_inscripcion DATE,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante),
    FOREIGN KEY (id_actividad) REFERENCES actividad(id_actividad)
);

CREATE TABLE asistencia (
    id_asistencia INT AUTO_INCREMENT PRIMARY KEY,
    id_inscripcion INT,
    fecha DATE,
    asistio BOOLEAN,
    FOREIGN KEY (id_inscripcion) REFERENCES inscripcion(id_inscripcion)
);


INSERT INTO estudiante (documento, nombre, apellido, email, carrera, facultad) VALUES
('12376392', 'Ana', 'Pérez', 'ana1@mail.com', 'Ingeniería', 'FING'),
('55684329', 'Juan', 'Gómez', 'juan1@mail.com', 'Contador', 'FCEA'),
('54426493', 'Lucía', 'Rodríguez', 'lucia1@mail.com', 'Derecho', 'FDER'),
('43390867', 'Martín', 'Fernández', 'martin1@mail.com', 'Ingeniería', 'FING'),
('28539041', 'Valentina', 'Silva', 'vale1@mail.com', 'Medicina', 'FMED'),
('39065190', 'Sofía', 'López', 'sofia1@mail.com', 'Psicología', 'FPSI'),
('44788620', 'Diego', 'Martínez', 'diego1@mail.com', 'Contador', 'FCEA'),
('52196552', 'Camila', 'Suárez', 'camila1@mail.com', 'Ingeniería', 'FING'),
('18725539', 'Nicolás', 'Pérez', 'nico1@mail.com', 'Derecho', 'FDER'),
('29974326', 'Florencia', 'García', 'flor1@mail.com', 'Medicina', 'FMED'),
('51890538', 'Ana', 'López', 'ana2@mail.com', 'Ingeniería', 'FING'),
('36648921', 'Juan', 'Silva', 'juan2@mail.com', 'Contador', 'FCEA'),
('45579227', 'Lucía', 'Martínez', 'lucia2@mail.com', 'Psicología', 'FPSI'),
('62339815', 'Martín', 'Suárez', 'martin2@mail.com', 'Derecho', 'FDER'),
('46788243', 'Valentina', 'Fernández', 'vale2@mail.com', 'Ingeniería', 'FING');

INSERT INTO disciplina (nombre) VALUES
('Fútbol'),
('Básquetbol'),
('Atletismo'),
('Vóleibol'),
('Yoga'),
('Funcional'),
('Gimnasio'),
('Fútbol'),
('Yoga'),
('Funcional'),
('Básquetbol'),
('Atletismo'),
('Vóleibol'),
('Gimnasio'),
('Fútbol');

INSERT INTO espacio (nombre, ubicacion, capacidad) VALUES
('Cancha Principal', 'Campus Norte', 50),
('Gimnasio Central', 'Campus Norte', 100),
('Sala Yoga A', 'Campus Sur', 30),
('Cancha Principal', 'Campus Norte', 50),
('Pista Atletismo', 'Campus Sur', 80),
('Sala Funcional', 'Campus Este', 40),
('Cancha Básquet', 'Campus Norte', 40),
('Sala Yoga A', 'Campus Sur', 30),
('Gimnasio Central', 'Campus Norte', 100),
('Cancha Vóley', 'Campus Oeste', 30),
('Pista Atletismo', 'Campus Sur', 80),
('Sala Funcional', 'Campus Este', 40),
('Cancha Básquet', 'Campus Norte', 40),
('Cancha Principal', 'Campus Norte', 50),
('Gimnasio Central', 'Campus Norte', 100);

INSERT INTO actividad (nombre_actividad, id_disciplina, id_espacio, cupo_max, dia, horario, estado) VALUES
('Fútbol Recreativo Mixto', 1, 1, 30, 'Lunes', '18:00:00', 'Abierta'),
('Básquet Inicial', 2, 7, 20, 'Martes', '19:00:00', 'Abierta'),
('Atletismo Inicial', 3, 5, 25, 'Miércoles', '17:00:00', 'Abierta'),
('Yoga Mañana', 5, 3, 20, 'Jueves', '09:00:00', 'Abierta'),
('Funcional Turno Mañana', 6, 6, 15, 'Viernes', '08:00:00', 'Abierta'),
('Gimnasio Libre', 7, 2, 50, 'Lunes', '10:00:00', 'Abierta'),
('Vóleibol Recreativo', 4, 10, 20, 'Martes', '18:00:00', 'Abierta'),
('Fútbol Recreativo Mixto', 1, 1, 30, 'Miércoles', '18:00:00', 'Abierta'),
('Yoga Tarde', 5, 8, 20, 'Jueves', '17:00:00', 'Abierta'),
('Funcional Avanzado', 6, 12, 15, 'Viernes', '19:00:00', 'Abierta'),
('Atletismo Intermedio', 3, 11, 25, 'Lunes', '16:00:00', 'Cerrada'),
('Básquet Intermedio', 2, 13, 20, 'Martes', '20:00:00', 'Abierta'),
('Gimnasio Libre', 7, 15, 50, 'Miércoles', '11:00:00', 'Finalizada'),
('Yoga Mañana', 5, 3, 20, 'Viernes', '09:00:00', 'Abierta'),
('Fútbol Competitivo', 1, 14, 22, 'Sábado', '10:00:00', 'Abierta');

INSERT INTO inscripcion (id_estudiante, id_actividad, estado_inscripcion, fecha_inscripcion) VALUES
(1, 1, 'Confirmada', '2026-06-01'),
(2, 1, 'Confirmada', '2026-06-01'),
(3, 2, 'Confirmada', '2026-06-02'),
(4, 3, 'Confirmada', '2026-06-02'),
(5, 4, 'Confirmada', '2026-06-03'),
(6, 5, 'Confirmada', '2026-06-03'),
(7, 6, 'Confirmada', '2026-06-04'),
(8, 7, 'Lista de espera', '2026-06-04'),
(9, 1, 'Confirmada', '2026-06-05'),
(10, 2, 'Confirmada', '2026-06-05'),
(11, 4, 'Confirmada', '2026-06-06'),
(12, 8, 'Lista de espera', '2026-06-06'),
(13, 9, 'Confirmada', '2026-06-07'),
(14, 10, 'Confirmada', '2026-06-07'),
(15, 15, 'Confirmada', '2026-06-08');

INSERT INTO asistencia (id_inscripcion, fecha, asistio) VALUES
(1, '2026-06-10', TRUE),
(2, '2026-06-10', TRUE),
(3, '2026-06-10', FALSE),
(4, '2026-06-11', TRUE),
(5, '2026-06-11', TRUE),
(6, '2026-06-12', FALSE),
(7, '2026-06-12', TRUE),
(8, '2026-06-12', FALSE),
(9, '2026-06-13', TRUE),
(10, '2026-06-13', TRUE),
(11, '2026-06-14', FALSE),
(12, '2026-06-14', FALSE),
(13, '2026-06-15', TRUE),
(14, '2026-06-15', TRUE),
(15, '2026-06-16', TRUE);