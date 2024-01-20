USE classicmodels;

# 초급
-- 1
INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, city, country)
VALUES (1, 'John', 'Doe', 'John', '010', 'dfj', 'sldkf', 'ddf');

-- 2
INSERT INTO products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP)
VALUES (1, 'dfk', 'Planes', 'sdlkfj', 'djf', 'sdjf', 1, 123, 123);

-- 3
INSERT INTO employees (employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle)
VALUES (1, 'dkf', 'as', 'dfj', 'dkjf', 1, 1625, "dfjk");

-- 4
INSERT INTO offices (officeCode, city, phone, addressLine1, country, postalCode, territory)
VALUES (8, 'city', 'phone', 'add', 'con', 'pos', 'ter');

-- 5
INSERT INTO orders (orderNumber, orderDate, requiredDate, status, customerNumber)
VALUES (1011, '2005-05-31', '2005-05-31', 'sta', 484);

-- 6
INSERT INTO orderdetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber)
VALUES (1011, 'S72_3212', 1, 343, 2);

-- 7
INSERT INTO payments (customerNumber, checkNumber, paymentDate, amount)
VALUES (211, 'MN89921', '2005-05-25', 123);

-- 8
INSERT INTO productlines (productLine)
VALUES ('Cars');

-- 9
INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, city, country)
VALUES (2, 'Jane', 'Smith', 'Jad', '010', 'dfj', 'New York', 'ddf');

-- 10
INSERT INTO products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP)
VALUES (2, 'dfk', 'Vintage Cars', 'sdlkfj', 'djf', 'sdjf', 1, 123, 123);

# 중급
-- 1
INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, city, country)
VALUES 
	(3, 'Bob', 'Brown', 'Jad', '010', 'dfj', 'New York', 'ddf'),
	(4, 'Sue', 'White', 'Jad', '010', 'dfj', 'New York', 'ddf');

-- 2
INSERT INTO products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP)
VALUES 
	(3, 'dfk', 'Classic Cars', 'sdlkfj', 'djf', 'sdjf', 1, 123, 123),
	(4, 'dfk', 'Motorcycles', 'sdlkfj', 'djf', 'sdjf', 1, 123, 123);

-- 3
INSERT INTO employees (employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle)
VALUES 
	(2, 'dkf', 'as', 'dfj', 'dkjf', 1, 1501, "dfjk"),
	(3, 'dkf', 'as', 'dfj', 'dkjf', 1, 1323, "dfjk");

-- 4
INSERT INTO orders (orderNumber, orderDate, requiredDate, status, customerNumber)
VALUES (1013, '2005-05-31', '2005-05-31', 'sta', 484);
INSERT INTO orderdetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber)
VALUES (1013, 'S72_3212', 1, 343, 2);

-- 5
INSERT INTO payments (customerNumber, checkNumber, paymentDate, amount)
VALUES
	(211, 'MB342426', '2005-05-25', 123),
	(211, 'FN155234', '2005-05-25', 123);

-- 6
INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, city, country)
VALUES (5, 'Tom', 'Black', 'Jad', '010', 'dfj', 'New York', 'ddf');
INSERT INTO orders (orderNumber, orderDate, requiredDate, status, customerNumber)
VALUES (1012, '2005-05-31', '2005-05-31', 'sta', 5);

-- 7
INSERT INTO employees (employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle)
VALUES (7, 'dkf', 'as', 'dfj', 'dkjf', 1, 1625, "dfjk");
UPDATE employees 
SET jobTitle = 'Sales Rep' 
WHERE employeeNumber = 7;

-- 8
INSERT INTO products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP)
VALUES ('S72_3213', 'dfk', 'Vintage Cars', 'sdlkfj', 'djf', 'sdjf', 1, 123, 123);
UPDATE products 
SET quantityInStock = 30 
WHERE productCode = 'S72_3213';

-- 9
INSERT INTO offices (officeCode, city, phone, addressLine1, country, postalCode, territory)
VALUES (9, 'city', 'phone', 'add', 'con', 'pos', 'ter');
UPDATE employees 
SET officeCode = 9 
WHERE lastName = 'Fixter';

-- 10
INSERT INTO productlines (productLine)
VALUES ('Bicycle');
INSERT INTO products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP)
VALUES
	(8, 'dfk', 'Bicycle', 'sdlkfj', 'djf', 'sdjf', 1, 123, 123),
	(9, 'dfk', 'Bicycle', 'sdlkfj', 'djf', 'sdjf', 1, 123, 123);

# 고급
-- 1
INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, city, country)
VALUES (9, 'Linda', 'Grey', 'Jad', '010', 'dfj', 'New York', 'ddf');
INSERT INTO orders (orderNumber, orderDate, requiredDate, status, customerNumber)
VALUES (3333, '2005-05-31', '2005-05-31', 'sta', 9);
INSERT INTO orderdetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber)
VALUES (3333, 'S72_3212', 1, 343, 2);

-- 2
INSERT INTO employees (employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle)
VALUES (10, 'Rachel', 'Purple', 'dfj', 'dkjf', 1, 1625, "dfjk");
UPDATE employees 
SET reportsTo = 1501
WHERE lastName = 'Rachel';

-- 3
INSERT INTO products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP)
VALUES ('S72_3215', 'dfk', 'Trains', 'sdlkfj', 'djf', 'sdjf', 1, 123, 123);
INSERT INTO orders (orderNumber, orderDate, requiredDate, status, customerNumber)
VALUES (1015, '2005-05-31', '2005-05-31', 'sta', 484);
INSERT INTO orderdetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber)
VALUES (1015, 'S72_3215', 1, 343, 2);

-- 4
INSERT INTO orders (orderNumber, orderDate, requiredDate, status, customerNumber)
VALUES (1017, '2005-05-31', '2005-05-31', 'sta', 484);
INSERT INTO payments (customerNumber, checkNumber, paymentDate, amount)
VALUES (484, 'MN89921', '2005-05-31', 123);

-- 5
INSERT INTO orderdetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber)
VALUES (10399, 'S72_1253', 10, 343, 2);
UPDATE products 
SET quantityInStock = quantityInStock - 10 
WHERE productCode = 'S72_1253';
