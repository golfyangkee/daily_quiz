-- 코드를 입력하세요
SELECT ANIMAL_ID, A.NAME
FROM ANIMAL_OUTS A JOIN ANIMAL_INS B USING(ANIMAL_ID)
WHERE A.DATETIME < B.DATETIME
ORDER BY B.DATETIME;