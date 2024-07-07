-- Create table for ingredients
CREATE TABLE ingredients (
    ingredient_id INTEGER PRIMARY KEY,
    ingredient_name TEXT NOT NULL UNIQUE,
    price_per_unit REAL NOT NULL -- Assuming price per pound or similar unit
);

-- Insert sample ingredient data
INSERT INTO ingredients (ingredient_name, price_per_unit) VALUES
    ('Cocoa', 5.00),
    ('Sugar', 2.00);

-- Create table for donuts
CREATE TABLE donuts (
    donut_id INTEGER PRIMARY KEY,
    donut_name TEXT NOT NULL,
    gluten_free INTEGER DEFAULT 0, -- 0 for false, 1 for true
    price_per_donut REAL NOT NULL
);

-- Create table for donut-ingredient relationships
CREATE TABLE donut_ingredients (
    donut_id INTEGER,
    ingredient_id INTEGER,
    FOREIGN KEY (donut_id) REFERENCES donuts(donut_id),
    FOREIGN KEY (ingredient_id) REFERENCES ingredients(ingredient_id),
    PRIMARY KEY (donut_id, ingredient_id)
);

-- Create table for customers
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

-- Create table for orders
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create table for order details (donuts in each order)
CREATE TABLE order_details (
    order_id INTEGER,
    donut_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (donut_id) REFERENCES donuts(donut_id),
    PRIMARY KEY (order_id, donut_id)
);

-- Insert sample data for donuts
INSERT INTO donuts (donut_name, gluten_free, price_per_donut) VALUES
    ('Belgian Dark Chocolate', 0, 4.00),
    ('Back-To-School Sprinkles', 0, 4.00);

-- Insert sample data for donut-ingredient relationships
INSERT INTO donut_ingredients (donut_id, ingredient_id) VALUES
    (1, 1), -- Belgian Dark Chocolate: Cocoa
    (1, 2), -- Belgian Dark Chocolate: Sugar
    (2, 2), -- Back-To-School Sprinkles: Sugar
    (2, 3), -- Back-To-School Sprinkles: Flour
    (2, 4); -- Back-To-School Sprinkles: Sprinkles

-- Insert sample data for customers
INSERT INTO customers (first_name, last_name) VALUES
    ('Luis', 'Singh');

-- Insert sample data for orders
INSERT INTO orders (order_id, customer_id) VALUES
    (1, 1); -- Order 1 by Luis Singh

-- Insert sample data for order details
INSERT INTO order_details (order_id, donut_id, quantity) VALUES
    (1, 1, 3), -- 3 Belgian Dark Chocolate
    (1, 2, 2); -- 2 Back-To-School Sprinkles
