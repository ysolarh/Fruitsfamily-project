-- 위 - 정답 보기 전, 아래 - 정답 본 후

USE sakila;

-- 데이터 조회 및 필터링
--  특정 배우가 출연한 영화 목록 조회
SELECT f.title 
FROM film_actor a 
JOIN film f ON a.film_id = f.film_id 
WHERE a.actor_id = ( 
	SELECT actor_id 
    FROM actor 
    WHERE first_name = 'PENELOPE' AND last_name = 'GUINESS'
);

SELECT f.title
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE a.first_name = 'PENELOPE' AND a.last_name = 'GUINESS';

--  모든 카테고리와 해당 카테고리의 영화 수 조회
SELECT c.category_id, c.name, COUNT(*)
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
GROUP BY c.category_id;

--  특정 고객의 대여 기록 조회
SELECT r.*
FROM rental r
JOIN customer c ON r.customer_id = c.customer_id
WHERE c.customer_id = 5;

SELECT r.customer_id, f.title, r.rental_date, r.return_date
FROM rental r 
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE r.customer_id = 5;

--  가장 최근에 추가된 10개의 영화 조회
SELECT release_year, title, last_update
FROM film
ORDER BY last_update DESC
LIMIT 10;

SELECT release_year, title
FROM film
ORDER BY release_year DESC
LIMIT 10;

-- 조인 및 관계
--  특정 영화에 출연한 배우 목록 조회
SELECT a.first_name, a.last_name
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
WHERE fa.film_id = (
	SELECT film_id
    FROM film
    WHERE title = 'ACADEMY DINOSAUR'
);

SELECT a.first_name, a.last_name
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
JOIN film f ON fa.film_id = f.film_id
WHERE f.title = 'ACADEMY DINOSAUR';

--  특정 영화를 대여한 고객 목록 조회
SELECT c.first_name, c.last_name, r.rental_date
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON i.inventory_id = r.inventory_id
WHERE i.film_id = (
	SELECT film_id
    FROM film
    WHERE title = 'ACADEMY DINOSAUR'
);

SELECT c.first_name, c.last_name
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE f.title = 'ACADEMY DINOSAUR';

--  모든 고객과 그들이 가장 최근에 대여한 영화 조회
SELECT c.customer_id, c.first_name, c.last_name, f.title, MAX(r.rental_date) AS last_rental_date
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON i.inventory_id = r.inventory_id
JOIN film f ON f.film_id = i.film_id
GROUP BY c.customer_id, c.first_name, c.last_name, f.title;

--  각 영화별 평균 대여 기간 조회
SELECT f.title, AVG(DATEDIFF(r.return_date, r.rental_date)) AS avg_rental_period
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
GROUP BY f.film_id;

-- 집계 및 그룹화
--  가장 많이 대여된 영화의 제목과 대여 횟수 조회
SELECT f.title, COUNT(r.rental_id) AS count_rental
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON r.inventory_id = i.inventory_id
GROUP BY f.film_id
ORDER BY count_rental DESC
LIMIT 1;

--  각 카테고리별 평균 대여 요금 조회
SELECT c.name, AVG(f.rental_rate) as avg_rental_rate
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN film f ON f.film_id = fc.film_id
GROUP BY c.category_id;

--  월별 총 매출 조회
SELECT YEAR(payment_date) AS year, MONTH(payment_date) AS month, SUM(amount) AS sum
FROM payment
GROUP BY year, month;

--  각 배우별 출연한 영화 수 조회
SELECT a.first_name, a.last_name, COUNT(fa.film_id) AS count
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
GROUP BY fa.actor_id;

-- 서브쿼리 및 고급 기능
--  가장 수익이 많은 영화 조회
SELECT f.title, SUM(p.amount) AS revenue
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN payment p ON r.rental_id = p.rental_id
GROUP BY f.film_id
ORDER BY revenue DESC
LIMIT 1;

--  평균 대여 요금보다 높은 요금의 영화 조회
SELECT title, rental_rate
FROM film
WHERE rental_rate > (
	SELECT AVG(rental_rate)
    FROM film
);

--  가장 활동적인 고객 조회
SELECT c.first_name, c.last_name, COUNT(r.rental_id) AS count_rental
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
GROUP BY c.customer_id
ORDER BY count_rental DESC
LIMIT 1;

--  특정 배우가 출연한 영화 중 가장 인기 있는 영화 조회
SELECT f.title, COUNT(r.rental_id) AS count_rental
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN film_actor fa ON f.film_id = fa.film_id
WHERE fa.actor_id = 1
GROUP BY fa.film_id
ORDER BY count_rental DESC
LIMIT 1;

-- 데이터 수정 및 관리
--  새로운 영화 추가
INSERT INTO film (title, language_id, rental_duration, rental_rate, replacement_cost, last_update)
VALUES ('old guard2', 1, 3, 5, 23, '2024-01-30 05:03:42');

--  고객 정보 업데이트
UPDATE customer
SET address_id = (
	SELECT address_id
    FROM address
    WHERE address = '1121 Loja Avenue'
)
WHERE customer_id = 5;

--  영화 대여 상태 변경
UPDATE rental
SET return_date = NOW()
WHERE rental_id = 200;

--  배우 정보 삭제
ALTER TABLE film_actor
ADD FOREIGN KEY (actor_id)
REFERENCES actor (actor_id)
ON DELETE CASCADE;
DELETE FROM actor
WHERE actor_id = 10;