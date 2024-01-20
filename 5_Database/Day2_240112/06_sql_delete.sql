USE classicmodels;

# 초급
-- 1
DELETE FROM customers
WHERE customerNumber = 3;

-- 2
DELETE FROM products
WHERE productCode = '2';

-- 3
DELETE FROM employees
WHERE employeeNumber = 2;

-- 4
DELETE FROM offices
WHERE officeCode = 10;

-- 5
DELETE FROM orders
WHERE orderNumber = 1012;

-- 6
DELETE FROM orderdetails
WHERE orderNumber = 1013;

-- 7
DELETE FROM payments
WHERE customerNumber = 1;

-- 8
DELETE FROM productlines
WHERE productLine = 'Cars';

-- 9
DELETE FROM customers
WHERE city = 'T';

-- 10
DELETE FROM products
WHERE productLine = 'Cars';

# 중급
-- 1 - department 없음
DELETE FROM employees
WHERE reportsTo = 1625;

-- 2
DELETE FROM offices
WHERE country = 'cons';

-- 3
DELETE FROM orders
WHERE orderDate BETWEEN '2023-12-01' AND '2023-12-31';

-- 4
DELETE FROM orderdetails
WHERE orderNumber = 1015;

-- 5
DELETE FROM payments
WHERE customerNumber = 2;

-- 6
DELETE FROM productlines
WHERE productLine IN ('Cars', 'Board');

-- 7 - mysql 이 버전에서는 서브쿼리에 limit 못써서 임시테이블 안에 넣어야함
DELETE FROM customers
WHERE customerNumber IN (
	SELECT * 
	FROM (
		SELECT customerNumber
		FROM customers
		ORDER BY customerNumber
		LIMIT 1
	) as t
);

-- 8
DELETE FROM products
WHERE quantityInStock = 0;

-- 9
DELETE FROM employees
WHERE jobTitle = 'dfjk';

-- 10 - officeSize 없음
DELETE FROM offices
WHERE officeCode < 0;

# 고급
-- 1
DELETE FROM orders
WHERE orderDate BETWEEN '2023-01-01' AND '2023-12-31';

-- 2
DELETE FROM orderdetails
WHERE productCode IN (
	SELECT *
	FROM (
		SELECT productCode
		FROM products
		ORDER BY quantityInStock ASC
		LIMIT 1
	) as t
);

-- 3
DELETE FROM payments
WHERE amount < 1;

-- 4
DELETE FROM productlines
WHERE productLine NOT IN (
	SELECT DISTINCT productLine
	FROM products
);

-- 5 - lastOrderDate 없음
DELETE FROM customers
WHERE creditLimit < 1;
