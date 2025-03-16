DROP DATABASE IF EXISTS boujee_salon;
CREATE DATABASE boujee_salon;
USE boujee_salon;

DROP TABLE IF EXISTS prices;
DROP TABLE IF EXISTS services;

CREATE TABLE services (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE prices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    service_id INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (service_id) REFERENCES services(id)
);

INSERT INTO services (name) VALUES
('Braiding'),
('Washing'),
('Drying'),
('Hair Removal'),
('Hair Treatment'),
('Hair Cut'),
('Hair Coloring'),
('Hair Extension'),
('Hair Styling'),
('Consultation');

-- Insert sample data for prices (not very pricey hehe)
INSERT INTO prices (service_id, price) VALUES
(1, 120.00),
(2, 20.00),
(3, 10.00),
(4, 5.00),
(5, 50.00),
(6, 35.00),
(7, 75.00),
(8, 150.00),
(9, 45.00),
(10, 0.00);

-- SELECT * FROM services;
-- SELECT * FROM prices;
