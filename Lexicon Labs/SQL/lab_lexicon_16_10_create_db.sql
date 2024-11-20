-- Assignment 1:

CREATE DATABASE IF NOT EXISTS clinic;
USE clinic;

CREATE TABLE departments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50)
);

INSERT INTO departments(name) VALUES('Therapy'), ('Support'), ('Management'),('Other');

CREATE TABLE employess (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    job_title VARCHAR(50) NOT NULL,
    department_id INT NOT NULL,
    salary DOUBLE NOT NULL,
    CONSTRAINT department_id FOREIGN KEY (department_id) REFERENCES departments(id)
);

INSERT INTO employees (first_name, last_name, job_title, department_id, salary) VALUES
    ('Maria', 'Anderson', 'Therapist', 1, 400.00),
    ('Anna', 'Johansson', 'Acupuncturist', 1, 830.00),
    ('Ingrid', 'Petterson', 'Technician', 2, 1140.00),
    ('Lena', 'Magnusson', 'Supervisor', 3, 1200.00),
    ('Sandy', 'Petersson', 'Dentist', 4, 1400.23),
    ('Max', 'Persson', 'Therapist', 1, 992.00),
    ('Anders', 'Tegnell', 'Epidemiologist', 4, 1340.00),
    ('Margareta', 'Olsson', 'Medical Director', 3, 2500.00),
    ('Daniel', 'Nilsson', 'AcNutrition Technician', 4, 2600.00);

CREATE TABLE rooms (
    id INT PRIMARY KEY AUTO_INCREMENT,
    occupation VARCHAR(30)
);

INSERT INTO rooms(occupation) VALUES ('free'), ('occupied'), ('free'), ('free'), ('occupied');

CREATE TABLE patients (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    room_id INT NOT NULL
);

INSERT INTO patients(first_name, last_name, room_id) VALUES
    ('Birgitta', 'Lasrsson', 1),
    ('Marianne', 'Lindeberg', 3),
    ('Bertil', 'Dahlberg', 2),
    ('Filip', 'Willhelm', 2),
    ('Nikolas', 'Nikolaev', 3);