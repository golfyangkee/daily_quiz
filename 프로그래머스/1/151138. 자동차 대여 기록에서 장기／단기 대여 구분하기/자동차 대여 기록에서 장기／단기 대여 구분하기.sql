SELECT HISTORY_ID, CAR_ID, DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE, DATE_FORMAT(END_DATE, '%Y-%m-%d') AS END_DATE, CASE WHEN DATEDIFF(END_DATE, START_DATE) >= 29 THEN '장기 대여'
        ELSE '단기 대여' END AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
WHERE START_DATE LIKE '2022-09%'
ORDER BY HISTORY_ID DESC;
# 하루를 빌리면 1이 나와야 하는데 빼면 0이 나오니까 30일 이상이 아니라 29일 이상으로 하면 된다.