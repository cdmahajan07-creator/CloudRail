USE CloudRail;

-- 1. Insert Stations
INSERT INTO stations (station_code, station_name, city) VALUES
('PUNE', 'Pune Junction', 'Pune'),
('CSMT', 'Chhatrapati Shivaji Maharaj Terminus', 'Mumbai'),
('NDLS', 'New Delhi Railway Station', 'New Delhi'),
('ADI', 'Ahmedabad Junction', 'Ahmedabad');

-- 2. Insert Trains
INSERT INTO trains (train_number, train_name, total_seats) VALUES
('12124', 'Deccan Queen Express', 120),
('12263', 'Hazrat Nizamuddin Duronto', 150),
('22943', 'Vande Bharat Express', 160);

-- 3. Insert Schedules
INSERT INTO schedules (train_id, source_station_id, destination_station_id, departure_time, arrival_time, fare) VALUES
(1, 1, 2, '2026-11-01 07:15:00', '2026-11-01 10:25:00', 380.00), -- Pune to CSMT
(2, 1, 3, '2026-11-01 11:10:00', '2026-11-02 06:55:00', 2100.00), -- Pune to New Delhi
(3, 1, 4, '2026-11-01 14:30:00', '2026-11-01 22:45:00', 1250.00); -- Pune to Ahmedabad