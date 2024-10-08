SELECT AI.ANIMAL_ID, AI.NAME
FROM ANIMAL_INS AI JOIN ANIMAL_OUTS AO USING(ANIMAL_ID)
WHERE AO.DATETIME IS NOT NULL 
ORDER BY DATEDIFF(AO.DATETIME, AI.DATETIME) DESC LIMIT 2;
