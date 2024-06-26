-- 푸드별 가장 많은 즐겨찾기 수 출력
# SELECT FOOD_TYPE, MAX(FAVORITES) AS FAVORITES
# FROM REST_INFO 
# GROUP BY FOOD_TYPE;

-- 정답
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO 
WHERE (FOOD_TYPE, FAVORITES) IN (SELECT FOOD_TYPE, MAX(FAVORITES) AS FAVORITES
                                FROM REST_INFO 
                                GROUP BY FOOD_TYPE)
ORDER BY 1 DESC;