USE classicmodels;

# 초급
-- 1
SELECT * FROM customers;

-- 2
SELECT * FROM products;

-- 3
SELECT firstName, lastName, jobTitle 
FROM employees;

-- 4
SELECT officeCode, city, addressLine1, addressLine2 state, country FROM offices;

-- 5
SELECT *
FROM orders
ORDER BY orderDate DESC
LIMIT 10;

-- 6
SELECT * 
FROM orderdetails
WHERE orderNumber = 1015;

-- 7
SELECT * 
FROM payments
WHERE customerNumber = 471;

-- 8
SELECT productLine, textDescription 
FROM productlines;

-- 9
SELECT * 
FROM customers
WHERE city = "New York";

-- 10
SELECT * 
FROM products
WHERE buyPrice BETWEEN 20 AND 50;;

# 중급
-- 1
SELECT * 
FROM orders 
WHERE customerNumber = '103';

-- 2
SELECT * 
FROM orderdetails
WHERE productCode = 'S72_3212';

-- 3
SELECT * 
FROM payments
WHERE paymentDate BETWEEN '2003-01-01' AND '2004-01-01';

-- 4
SELECT firstName, lastName, jobTitle
FROM employees
WHERE jobTitle = 'Sales Rep';

-- 5
SELECT *
FROM offices
WHERE country = 'USA';

-- 6
SELECT *
FROM products
WHERE productLine = 'Classic Cars';

-- 7
SELECT *
FROM customers
ORDER BY customerNumber DESC
LIMIT 5;

-- 8
SELECT *
FROM products
WHERE quantityInStock < 10;

-- 9
SELECT *
FROM orders
WHERE orderDate BETWEEN '2023-12-01' AND '2023-12-31';

-- 10
SELECT orderNumber, SUM(quantityOrdered * priceEach) AS totalAmount
FROM orderdetails
WHERE orderNumber = 10101;

# 고급
-- 1
SELECT city, COUNT(*) AS customerCount
FROM customers
GROUP BY city;

-- 2
SELECT productLine, AVG(buyPrice) AS averagePrice
FROM products
GROUP BY productLine;

-- 3
SELECT officeCode, COUNT(*) AS employeeCount
FROM employees
GROUP BY officeCode;

-- 4 - salary 비슷한것도 없는것 같은데...
SELECT officeCode, AVG(salary) AS averageSalary
FROM employees
GROUP BY officeCode;

-- 5
SELECT productCode, SUM(quantityOrdered) AS totalOrdered
FROM orderdetails
GROUP BY productCode
ORDER BY totalOrdered DESC
LIMIT 5;
