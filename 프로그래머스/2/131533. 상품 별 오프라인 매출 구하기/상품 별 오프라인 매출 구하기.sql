SELECT PRODUCT_CODE, PRICE*SUM(SALES_AMOUNT) AS SALES
FROM PRODUCT P JOIN OFFLINE_SALE OS USING (PRODUCT_ID)
GROUP BY PRODUCT_CODE
ORDER BY 2 DESC, 1;