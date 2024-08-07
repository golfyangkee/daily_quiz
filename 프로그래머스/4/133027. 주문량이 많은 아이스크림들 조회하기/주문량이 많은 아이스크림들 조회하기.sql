-- 7월 맛별 총 주문량 출력
# SELECT FLAVOR, SUM(TOTAL_ORDER)
# FROM JULY 
# GROUP BY FLAVOR;
-- 상반기 맛별 총 주문량 출력
# SELECT FLAVOR, SUM(TOTAL_ORDER)
# FROM FIRST_HALF 
# GROUP BY FLAVOR;
-- 정답
SELECT FLAVOR
FROM FIRST_HALF FH JOIN JULY J USING(FLAVOR)
GROUP BY FLAVOR
ORDER BY SUM(FH.TOTAL_ORDER)+SUM(J.TOTAL_ORDER) DESC LIMIT 3;

-- JULY 총 주문량 상위 3개
# SELECT FLAVOR, SUM(TOTAL_ORDER) AS AMOUNT
# FROM JULY
# GROUP BY FLAVOR

-- FIRST_HALF 랑 합치기
# SELECT FLAVOR
# FROM FIRST_HALF A JOIN (SELECT FLAVOR, SUM(TOTAL_ORDER) AS AMOUNT
#                         FROM JULY
#                         GROUP BY FLAVOR) B USING (FLAVOR)
# ORDER BY (A.TOTAL_ORDER+B.AMOUNT) DESC LIMIT 3;