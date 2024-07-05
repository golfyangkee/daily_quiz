SELECT AI.NAME, AI.DATETIME
FROM ANIMAL_INS AI LEFT JOIN ANIMAL_OUTS AO USING(ANIMAL_ID)
WHERE AI.ANIMAL_ID IS NOT NULL AND AO.ANIMAL_ID IS NULL
ORDER BY 2 LIMIT 3;