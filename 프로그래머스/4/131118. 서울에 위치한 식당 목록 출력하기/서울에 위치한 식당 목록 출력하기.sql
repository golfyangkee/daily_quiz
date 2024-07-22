WITH SEOUL AS (
-- 서울 위치 식당 ID, 이름, 음식종류, 즐겨찾기수, 주소 출력
SELECT REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS
FROM REST_INFO 
# WHERE ADDRESS LIKE '%서울%'
WHERE ADDRESS LIKE '서울%'
ORDER BY 1
),
SCORE_TABLE AS (
-- 식당 아이디별 리뷰 평균 점수 조회
SELECT REST_ID, ROUND(AVG(REVIEW_SCORE),2) AS SCORE
FROM REST_REVIEW 
GROUP BY 1
ORDER BY 1
)

-- 합치기
SELECT REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, SCORE
FROM SEOUL S JOIN SCORE_TABLE T USING(REST_ID)
ORDER BY 6 DESC, 4 DESC;