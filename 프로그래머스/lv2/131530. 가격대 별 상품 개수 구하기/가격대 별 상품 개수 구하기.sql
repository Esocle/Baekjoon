-- 코드를 입력하세요
SELECT FLOOR(PRICE/10000)*10000 AS PRICE_GROUP, COUNT(PRODUCT_ID)
FROM PRODUCT
GROUP BY FLOOR(PRICE/10000)
ORDER BY FLOOR(PRICE/10000);