-- 코드를 입력하세요
WITH RECURSIVE tb1 AS (
    SELECT 0 AS HOUR
    UNION ALL
    SELECT HOUR+1 FROM tb1 WHERE HOUR < 23
), tb2 AS(
    SELECT HOUR(DATETIME) AS HOUR,
    COUNT(DISTINCT ANIMAL_ID) AS CNT
    FROM ANIMAL_OUTS
    GROUP BY HOUR
)

SELECT tb1.HOUR,
CASE WHEN tb2.CNT is NULL THEN 0 ELSE CNT END AS CNT
FROM tb1 LEFT JOIN tb2 ON tb1.HOUR = tb2.HOUR
ORDER BY HOUR;