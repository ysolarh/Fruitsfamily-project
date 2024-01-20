USE yes24;

CREATE TABLE Books (
    bookID INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255),
    publisher VARCHAR(255),
    publishing DATE,
    rating DECIMAL(3, 1),
    review INT,
    sales INT,
    price DECIMAL(10, 2),
    ranking INT,
    ranking_weeks INT
);


-- 기본 조회 및 필터링

--  모든 책의 제목과 저자를 조회하세요.
SELECT title, author 
FROM books;

--  평점이 8 이상인 책 목록을 조회하세요.
SELECT * 
FROM books 
WHERE rating >= 8.0;

--  리뷰 수가 100개 이상인 책들의 제목과 리뷰 수를 조회하세요.
SELECT title, review 
FROM books 
WHERE review >= 100 
ORDER BY review DESC;

--  가격이 20,000원 미만인 책들의 제목과 가격을 조회하세요.
SELECT title, price 
FROM books 
WHERE price < 20000;

--  국내도서TOP100에 4주 이상 머문 책들을 조회하세요.
SELECT * 
FROM books 
WHERE ranking_weeks >= 4 
ORDER BY ranking_weeks DESC;

--  특정 저자의 모든 책을 조회하세요.
SELECT * 
FROM books 
WHERE author = '자청 저';

--  특정 출판사가 출판한 책들을 조회하세요.
SELECT * 
FROM books 
WHERE publisher = '웅진지식하우스'


-- 조인 및 관계

--  저자별로 출판한 책의 수를 조회하세요.
SELECT author, COUNT(*) AS books_count 
FROM books 
GROUP BY author 
ORDER BY books_count DESC;

--  가장 많은 책을 출판한 출판사를 찾으세요.
SELECT publisher, COUNT(*) AS publishing_count 
FROM books 
GROUP BY publisher 
ORDER BY publishing_count DESC 
LIMIT 1;

--  가장 높은 평균 평점을 가진 저자를 찾으세요.
SELECT author, AVG(rating) AS rating_avg 
FROM books 
GROUP BY author 
ORDER BY rating_avg DESC
LIMIT 1;

--  국내도서랭킹이 1위인 책의 제목과 저자를 조회하세요.
SELECT * 
FROM books 
WHERE ranking = 1;

--  판매지수와 리뷰 수가 모두 높은 상위 10개의 책을 조회하세요.
SELECT title, sales, review 
FROM books 
ORDER BY sales DESC, review DESC 
LIMIT 10;

--  가장 최근에 출판된 5권의 책을 조회하세요.
SELECT * 
FROM books 
ORDER BY publishing DESC 
LIMIT 5;


-- 집계 및 그룹화

--  저자별 평균 평점을 계산하세요.
SELECT author, AVG(rating) AS rating_avg 
FROM books 
GROUP BY author 
ORDER BY rating_avg DESC;

--  출판일별 출간된 책의 수를 계산하세요.
SELECT publishing, COUNT(*) 
FROM books 
GROUP BY publishing;

--  책 제목별 평균 가격을 조회하세요.
SELECT title, AVG(price) 
FROM books 
GROUP BY title;

--  리뷰 수가 가장 많은 상위 5권의 책을 찾으세요.
SELECT * 
FROM books 
ORDER BY review DESC 
LIMIT 5;

--  국내도서랭킹 별 평균 리뷰 수를 계산하세요.
SELECT ranking, AVG(review) 
FROM books 
GROUP BY ranking;


-- 서브쿼리 및 고급 기능

--  평균 평점보다 높은 평점을 받은 책들을 조회하세요.
SELECT title, rating 
FROM books 
WHERE rating > (
	SELECT AVG(rating) 
	FROM books
) 
ORDER BY rating DESC;

--  평균 가격보다 비싼 책들의 제목과 가격을 조회하세요.
SELECT title, price, publisher 
FROM books 
WHERE price > (
	SELECT AVG(price) 
	FROM books
);

--  가장 많은 리뷰를 받은 책보다 많은 리뷰를 받은 다른 책들을 조회하세요.
SELECT title, review 
FROM books 
WHERE review > (
	SELECT MAX(review) 
	FROM books
);

--  평균 판매지수보다 낮은 판매지수를 가진 책들을 조회하세요.
SELECT title, sales 
FROM books 
WHERE sales < (
	SELECT AVG(sales) 
	FROM books
);

--  가장 많이 출판된 저자의 책들 중 최근에 출판된 책을 조회하세요.
SELECT author, title 
FROM books 
WHERE author = (
	SELECT author 
	FROM books 
	GROUP BY author 
	ORDER BY COUNT(*) DESC 
	LIMIT 1);


-- 데이터 수정 및 관리

--  특정 책의 가격을 업데이트하세요.
UPDATE books 
SET price = 9999 
WHERE title = "한국사";

--  특정 저자의 책 제목을 변경하세요.
UPDATE books 
SET title = '제목업데이트' 
WHERE author = '최태성 저';

--  판매지수가 가장 낮은 책을 데이터베이스에서 삭제하세요.
DELETE FROM books 
WHERE sales = (
	SELECT sales
	FROM (
		SELECT MIN(sales)
		FROM books
	) as t
);

--  특정 출판사가 출판한 모든 책의 평점을 1점 증가시키세요.
UPDATE books 
SET rating = rating + 1 
WHERE publisher = '웅진하우스';


-- 데이터 분석 예제

--  저자별 평균 평점 및 판매지수를 분석하여 인기 있는 저자를 확인합니다.
SELECT author, AVG(rating), AVG(sales) 
FROM books 
GROUP BY author 
ORDER BY AVG(rating) DESC, AVG(sales) DESC;

--  출판일에 따른 책 가격의 변동 추세를 분석합니다.
SELECT publishing, AVG(price) 
FROM books 
GROUP BY publishing 
ORDER BY publishing ASC;

--  출판사별 출간된 책의 수와 평균 리뷰 수를 비교 분석합니다.
SELECT publisher, COUNT(*) AS book_count, SUM(review) AS review_sum 
FROM books 
GROUP BY publisher 
ORDER BY book_count DESC;

--  국내도서랭킹과 판매지수의 상관관계를 분석합니다.
SELECT ranking, AVG(sales) 
FROM books 
GROUP BY ranking;

--  가격 대비 리뷰 수와 평점의 관계를 분석하여 가성비 좋은 책을 찾습니다.
SELECT price, AVG(review), AVG(rating) 
FROM books 
GROUP BY price;


-- 난이도 있는 문제

--  출판사별 평균 판매지수가 가장 높은 저자 찾기
SELECT publisher, author, AVG(sales) as avg_sales 
FROM books 
GROUP BY publisher, author 
ORDER BY publisher, avg_sales DESC;

--  리뷰 수가 평균보다 높으면서 가격이 평균보다 낮은 책 조회
SELECT title, review, price 
FROM books 
WHERE review > (
	SELECT AVG(review) 
	FROM books
) AND price < (
	SELECT AVG(price) 
	FROM books
);

--  가장 많은 종류의 책을 출판한 저자 찾기
SELECT author, COUNT(DISTINCT title) as num_books 
FROM books 
GROUP BY author 
ORDER BY num_books DESC 
LIMIT 1;

--  각 저자별로 가장 높은 판매지수를 기록한 책 조회
SELECT author, MAX(sales) AS max_sales 
FROM books 
GROUP BY author;

--  연도별 출판된 책 수와 평균 가격 비교
SELECT MONTH(publishing) AS month, COUNT(*) as num_books, AVG(price) AS avg_price 
FROM books 
GROUP BY month;

--  출판사가 같은 책들 중 평점 편차가 가장 큰 출판사 찾기
SELECT publisher, COUNT(*), MAX(rating) - MIN(rating) AS rating_difference 
FROM books 
GROUP BY publisher 
HAVING COUNT(*) >= 2 
ORDER BY rating_difference DESC 
LIMIT 1;

--  특정 저자의 책들 중 판매지수 대비 평점이 가장 높은 책 찾기
SELECT title, sales, rating / sales AS ratio 
FROM books 
WHERE author = '특정 저자'
ORDER BY ratio DESC
LIMIT 1;

