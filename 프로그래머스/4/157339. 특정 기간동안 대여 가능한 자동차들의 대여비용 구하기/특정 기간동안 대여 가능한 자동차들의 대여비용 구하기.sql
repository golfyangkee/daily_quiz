-- 1단계 : 자동차 종류 세단 SUV
# SELECT CAR_ID, CAR_TYPE, DAILY_FEE
# FROM CAR_RENTAL_COMPANY_CAR 
# WHERE CAR_TYPE IN ('세단', 'SUV');

-- 2단계 : 30일간 대여 금액이 50만원이상 200만원미만인 자동차 출력 = 3, 18, 23, 27
# SELECT CAR_ID, CAR_TYPE, DAILY_FEE, DAILY_FEE*30 AS FEE
# FROM CAR_RENTAL_COMPANY_CAR 
# WHERE CAR_TYPE IN ('세단', 'SUV')
#     AND (DAILY_FEE*30>=500000 AND 2000000> DAILY_FEE*30);

-- 3단계 : 2단계에서 할인을 적용해보자. - 3, 18, 23, 27
-- 세단 5, 8, 12  / SUV 3, 5, 10
# WITH F AS (
# SELECT CAR_TYPE, (1-DISCOUNT_RATE/100) AS DISCOUNT
# FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
# WHERE DURATION_TYPE = '30일 이상'
# )

# SELECT CAR_ID, CAR_TYPE, DAILY_FEE, ROUND(DAILY_FEE*30*DISCOUNT) AS FEE
# FROM CAR_RENTAL_COMPANY_CAR CRCC JOIN F USING (CAR_TYPE)
# WHERE CAR_TYPE IN ('세단', 'SUV') AND (DAILY_FEE*30*DISCOUNT>=500000 AND 2000000> DAILY_FEE*30*DISCOUNT);

-- 4단계 : 3단계 중 11월 한달간 대여 가능
WITH 
F AS ( # 30일 이상
SELECT CAR_TYPE, (1-DISCOUNT_RATE/100) AS DISCOUNT
FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
WHERE DURATION_TYPE = '30일 이상'
)

SELECT CAR_ID, CAR_TYPE, ROUND(DAILY_FEE*30*DISCOUNT) AS FEE
FROM CAR_RENTAL_COMPANY_CAR CRCC JOIN F USING (CAR_TYPE) 
WHERE CAR_TYPE IN ('세단', 'SUV') 
AND (DAILY_FEE*30*DISCOUNT>=500000 AND 2000000> DAILY_FEE*30*DISCOUNT)
AND CAR_ID NOT IN (
    SELECT DISTINCT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE START_DATE <= '2022-11-30' 
        AND END_DATE >= '2022-11-01');

-- 자동차 종류가 세단 SUV인 자동차 출력
# SELECT *
# FROM CAR_RENTAL_COMPANY_CAR 
# WHERE CAR_TYPE IN ('세단', 'SUV');
-- 2, 3, 4, 5, 9, 10, 14, 16, 17, 18, 19, 22, 23, 24, 25, 26, 27, 29
-- 18개

-- 30일이상 할인율 보기
# SELECT CAR_TYPE, DISCOUNT_RATE
# FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
# WHERE  DURATION_TYPE = '30일 이상';
-- 세단 8, SUV 5
-- 여기서 CAR_TYPE이랑 DISCOUNT_RATE 만 뽑아다가 쓰면 됨 

-- 2022년 11월 1일부터 2022년 11월 30일 기간 추후 부정할 예정
-- START_DATE <= 2022-11-30 AND END_DATE >= 2022-11-01
# SELECT DISTINCT CAR_ID
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
# WHERE DATE_FORMAT(START_DATE, '%Y-%m-%d') <= '2022-11-30' AND DATE_FORMAT(END_DATE, '%Y-%m-%d') >= '2022-11-01'
# ORDER BY 1;
-- 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 17, 18, 19, 20, 21, 22, 26, 27, 28, 29
-- 23개

-- 자동차 타입으로 CC랑 DP 합치기
-- 할인율 10%면 100-10 = 90%가 요금
-- (100-DISCOUNT_RATE)/100 = 요금비율
-- DAILY_FEE*30*((100-DISCOUNT_RATE)/100)
# SELECT CAR_ID, CAR_TYPE, ROUND(DAILY_FEE*30*(1-DISCOUNT_RATE*0.01)) AS FEE
# FROM CAR_RENTAL_COMPANY_CAR CC JOIN (SELECT CAR_TYPE, DISCOUNT_RATE
#                                     FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
#                                     WHERE DURATION_TYPE = '30일 이상') DP USING(CAR_TYPE)
# WHERE CAR_TYPE IN ('세단', 'SUV')
# AND DAILY_FEE*30*(1-DISCOUNT_RATE*0.01) >=500000 AND DAILY_FEE*30*(1-DISCOUNT_RATE*0.01) <2000000
# AND CAR_ID NOT IN 
# (SELECT DISTINCT CAR_ID
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
# WHERE DATE_FORMAT(START_DATE, '%Y-%m-%d') <= '2022-11-30' AND DATE_FORMAT(END_DATE, '%Y-%m-%d') >= '2022-11-01');
-- FEE 적용 안 하면 18개 나옴
-- FEE 적용하면 3, 18, 23, 27
-- 4개 나옴

-- 날짜 적용
-- 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 17, 18, 19, 20, 21, 22, 26, 27, 28, 29
-- 23개
-- 제외하면
-- 3, 23