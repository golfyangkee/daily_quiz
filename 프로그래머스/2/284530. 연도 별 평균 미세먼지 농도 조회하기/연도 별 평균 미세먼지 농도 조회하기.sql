-- 코드를 작성해주세요
SELECT YEAR(YM) AS YEAR, ROUND(AVG(PM_VAL1), 2) AS "PM10", ROUND(AVG(PM_VAL2), 2) AS "PM2.5"
FROM AIR_POLLUTION 
WHERE LOCATION2 = "수원"
GROUP BY YEAR(YM)
ORDER BY YEAR(YM);
-- YEAR 함수는 날짜 값에서 연도 부분만을 추출하여 정수로 반환
-- DATE_FORMAT 함수는 날짜 값에서 원하는 형식으로 날짜를 문자열로 반환