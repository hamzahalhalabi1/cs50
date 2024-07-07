-- Create the Passengers table
CREATE TABLE Passengers (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL
);

-- Create the CheckIns table
CREATE TABLE CheckIns (
    id INTEGER PRIMARY KEY,
    checkin_time DATETIME NOT NULL,
    passenger_id INTEGER NOT NULL,
    flight_id INTEGER NOT NULL,
    FOREIGN KEY (passenger_id) REFERENCES Passengers(id),
    FOREIGN KEY (flight_id) REFERENCES Flights(id)
);

-- Create the Airlines table
CREATE TABLE Airlines (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    concourse TEXT NOT NULL
);

-- Create the Flights table
CREATE TABLE Flights (
    id INTEGER PRIMARY KEY,
    flight_number TEXT NOT NULL,
    airline_id INTEGER NOT NULL,
    departure_airport TEXT NOT NULL,
    arrival_airport TEXT NOT NULL,
    departure_time DATETIME NOT NULL,
    arrival_time DATETIME NOT NULL,
    FOREIGN KEY (airline_id) REFERENCES Airlines(id)
);
