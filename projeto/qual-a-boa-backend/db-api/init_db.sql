-- Create the database
CREATE DATABASE restaurant_db;

-- Connect to the database
\c restaurant_db;

-- Create the restaurants table
CREATE TABLE restaurants (
    id SERIAL PRIMARY KEY,
    cnpj VARCHAR(18) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    state CHAR(2) NOT NULL,
    city VARCHAR(100) NOT NULL,
    type VARCHAR(50) NOT NULL,
    operating_hours VARCHAR(200),
    postal_code VARCHAR(9) NOT NULL,
    street_number VARCHAR(10) NOT NULL
);

-- Create the users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(128) NOT NULL
);

-- Create indexes for better performance
CREATE INDEX idx_restaurants_state ON restaurants(state);
CREATE INDEX idx_restaurants_city ON restaurants(city);
CREATE INDEX idx_restaurants_type ON restaurants(type);

-- Sample data (optional)
INSERT INTO restaurants (cnpj, name, state, city, type, operating_hours, postal_code, street_number)
VALUES
    ('12.345.678/0001-99', 'Italian Bistro', 'SP', 'São Paulo', 'Italian', 'Mon-Fri: 11:00-22:00, Sat-Sun: 12:00-23:00', '01234-567', '123'),
    ('98.765.432/0001-10', 'Brazilian Grill', 'RJ', 'Rio de Janeiro', 'Brazilian', 'Mon-Sun: 10:00-22:00', '20000-000', '456'),
    ('11.222.333/0001-44', 'Sushi Express', 'SP', 'São Paulo', 'Japanese', 'Tue-Sun: 18:00-23:00', '04567-890', '789'),
    ('44.555.666/0001-77', 'Taco House', 'MG', 'Belo Horizonte', 'Mexican', 'Mon-Sat: 11:00-23:00', '30000-000', '101'); 