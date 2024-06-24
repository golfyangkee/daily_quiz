-- 16일 대여
-- START_DATE< 16일 AND END_DATE >=16일 이면 대여 중
-- END_DATE가 16일 전 이거나, START_DATE가 16일 이후면 대여 가능
-- 
SELECT CAR_ID, CASE WHEN SUM(CASE WHEN '2022-10-16' BETWEEN START_DATE AND END_DATE THEN 1
ELSE 0 END) = 1 THEN '대여중' ELSE '대여 가능' 
END AS AVAILABILITY 
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY 1
ORDER BY 1 DESC;

# SELECT car_id,
# case when 
# sum(case when '2022-10-16' between start_date and end_date then 1
# else 0 end) =1 then '대여중'
# else '대여 가능'
# end availability
# from car_rental_company_rental_history
# group by 1
# order by 1 desc;