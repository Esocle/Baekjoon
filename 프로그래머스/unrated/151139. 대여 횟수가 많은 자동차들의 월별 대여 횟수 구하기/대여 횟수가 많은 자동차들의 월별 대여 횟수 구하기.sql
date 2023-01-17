-- 코드를 입력하세요
SELECT MONTH, CAR_ID, RECORDS
FROM (
    SELECT DISTINCT MONTH(START_DATE) AS MONTH,
    CAR_ID,
    COUNT(*) OVER(PARTITION BY MONTH(START_DATE), CAR_ID) AS RECORDS,
    COUNT(*) OVER(PARTITION BY CAR_ID) AS FILTER
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
    WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
)A
WHERE FILTER >= 5
ORDER BY MONTH ASC, CAR_ID DESC;