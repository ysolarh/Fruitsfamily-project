USE classicmodels;

# 초급
-- 1
UPDATE customers
SET addressLine1 = '456'
WHERE customerNumber = 1;

-- 2
UPDATE products
SET buyPrice = 29.99
WHERE productCode = '3';

-- 3
UPDATE employees
SET jobTitle = 'Manager'
WHERE employeeNumber = 1;

-- 4
UPDATE offices
SET phone = '123-456-7891'
WHERE officeCode = 1;

-- 5
UPDATE orders
SET status = 'Shipped'
WHERE orderNumber = 3333;

-- 6
UPDATE orderdetails
SET quantityOrdered = 3
WHERE orderNumber = 3333 AND productCode = 'S72_3212';

-- 7
UPDATE payments
SET amount = 250.00
WHERE customerNumber =211 AND paymentDate = '2003-12-09';

-- 8
UPDATE productlines
SET textDescription = 'Updated description'
WHERE productLine = 'Cars';

-- 9
UPDATE customers
SET phone = '2039203'
WHERE customerNumber = 1;

-- 10
UPDATE products
SET buyPrice = buyPrice * 1.1;

# 중급
-- 1
UPDATE employees
SET officeCode = 3
WHERE reportsTo = 1002;

-- 2
UPDATE offices
SET city = 'Updated City'
WHERE country = 'Japan';

-- 3
UPDATE orders
SET status = 'Cancelled'
WHERE orderDate BETWEEN '2023-01-01' AND '2023-01-31';

-- 4
UPDATE orderdetails
SET priceEach = priceEach * 0.9
WHERE orderNumber IN (
	SELECT orderNumber
	FROM orders
	WHERE orderDate BETWEEN '2023-01-01' AND '2023-01-31'
);

-- 5
UPDATE payments
SET amount = amount * 1.05
WHERE customerNumber = 484;

-- 6
UPDATE productlines
SET textDescription = 'New description'
WHERE productLine IN ('Bicycle', 'Cars');

-- 7
UPDATE customers
SET phone = '999-999-9999'
WHERE city = 'San Francisco';

-- 8
UPDATE products
SET buyPrice = buyPrice * 0.95
WHERE productLine = 'Classic Cars';

-- 9
UPDATE employees
SET email = 'dkfjkd@kdjfk'
WHERE employeeNumber = 1;

-- 10
UPDATE offices
SET addressLine1 = '1234 new', phone = '987-654-3211'
WHERE officeCode = 2;

# 고급
-- 1
UPDATE orders
SET status = 'On Hold'
WHERE orderDate BETWEEN '2022-01-01' AND '2022-12-31';

-- 2
UPDATE orderdetails
SET priceEach = priceEach * 1.1
WHERE orderNumber = 3333;

-- 3
UPDATE payments
SET paymentDate = '2023-02-01'
WHERE paymentDate BETWEEN '2023-01-01' AND '2023-01-31';

-- 4
UPDATE productlines
SET textDescription = 'New updated description'
WHERE productLine IN (
	SELECT productLine
	FROM products
	WHERE quantityInStock < 0
);

-- 5
UPDATE customers
SET addressLine2 = 'New add'
WHERE customerNumber BETWEEN 1 and 10;

