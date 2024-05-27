-- 이해가 안 됨, 해당 아이디의 8~10월까지만 세어야 해서, 조건 안 넣으면 전체 기간 카운팅
SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(*) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
WHERE MONTH(START_DATE) BETWEEN 8 AND 10 AND CAR_ID IN (SELECT CAR_ID
                 FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                 WHERE START_DATE BETWEEN "2022-08-01" AND "2022-10-31"
                 GROUP BY CAR_ID
                 HAVING COUNT(*) >=5)
GROUP BY MONTH, CAR_ID
ORDER BY 1, 2 DESC;