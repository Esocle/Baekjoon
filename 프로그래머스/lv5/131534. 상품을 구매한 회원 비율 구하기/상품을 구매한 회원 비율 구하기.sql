-- 코드를 입력하세요
SELECT YEAR(O.SALES_DATE) AS YEAR, MONTH(O.SALES_DATE) AS MONTH,
COUNT(DISTINCT U.USER_ID) AS PUCHASED_USERS,
ROUND(COUNT(DISTINCT U.USER_ID) / COUNT, 1) AS PUCHASED_RATIO
FROM ONLINE_SALE O INNER JOIN (
    SELECT USER_ID, COUNT(*) OVER() AS COUNT
    FROM USER_INFO
    WHERE JOINED BETWEEN '2021-01-01' AND '2021-12-31'
) U ON U.USER_ID = O.USER_ID
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH;