/*
This file contains a script of Transact SQL (T-SQL) command to interact with a database named 'Inventory'.
Requirements:
- referential integrity is enforced
Steps:
1) Check if the database 'Inventory' exists, if it does exist, drop it and create a new one.
2) Set the default database to 'Inventory'.
3) Create a 'suppliers' table. Use the following columns:
- id: integer, primary key
- name: 50 characters, not null
- address: 255 characters, nullable
- city: 50 characters, not null
- state: 2 characters, not null
- update_timestamp: datetime, default current_timestamp
4) Create the 'categories' table with a one-to-many relation to the 'suppliers'. Use the following columns:
- id:  integer, primary key
- name: 50 characters, not null
- description:  255 characters, nullable
- supplier_id: int, foreign key references suppliers(id)
5) Create the 'products' table with a one-to-many relation to the 'categories' table. Use the following columns:
- id: integer, primary key
- name: 50 characters, not null
- price: decimal (10, 2), not null
- category_id: int, foreign key references categories(id)
6) Populate the 'suppliers' table with sample data.
7) Populate the 'categories' table with sample data.
8) Populate the 'products' table with sample data.
9) Create a view named 'product_list' that displays the following columns:
- product_id
- product_name
- category_name
- supplier_name
*/

-- Step 1: Check if the database 'Inventory' exists, if it does exist, drop it and create a new one.
IF EXISTS (SELECT name FROM sys.databases WHERE name = 'Inventory')
BEGIN
    DROP DATABASE Inventory;
END
CREATE DATABASE Inventory;

-- Step 2: Set the default database to 'Inventory'.
USE Inventory;

-- Step 3: Create a 'suppliers' table.
CREATE TABLE suppliers (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    address VARCHAR(255) NULL,
    city VARCHAR(50) NOT NULL,
    state CHAR(2) NOT NULL,
    -- add a description column
    description VARCHAR(255) NULL,
    update_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    created_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Step 4: Create the 'categories' table with a one-to-many relation to the 'suppliers'.
CREATE TABLE categories (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(255) NULL,
    supplier_id INT,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(id),
    update_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    created_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Step 5: Create the 'products' table with a one-to-many relation to the 'categories'.
CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES categories(id),
    update_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    created_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Step 6: Populate the 'suppliers' table with sample data.
INSERT INTO suppliers (id, name, address, city, state, description)
VALUES (1, 'Supplier A', '123 Main St', 'Anytown', 'NY', 'Supplier A description'),
       (2, 'Supplier B', '456 Elm St', 'Otherville', 'CA', 'Supplier B description');

-- Step 7: Populate the 'categories' table with sample data.
INSERT INTO categories (id, name, description, supplier_id)
VALUES (1, 'Category A', 'Category A description', 1),
       (2, 'Category B', 'Category B description', 2);

-- Step 8: Populate the 'products' table with sample data.
INSERT INTO products (id, name, price, category_id)
VALUES (1, 'Product A', 10.00, 1),
       (2, 'Product B', 20.00, 2);

-- Step 9: Create a view named 'product_list' that displays the following columns.
CREATE VIEW product_list AS
SELECT p.id AS product_id, p.name AS product_name, c.name AS category_name, s.name AS supplier_name
FROM products p
JOIN categories c ON p.category_id = c.id
JOIN suppliers s ON c.supplier_id = s.id;

-- End of file


