-- 파이썬 씨샵 스킬코드 출력
# SELECT CODE
# FROM SKILLCODES 
# WHERE NAME IN ('Python', 'C#');

-- 정답
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS
WHERE SKILL_CODE & (SELECT CODE
                    FROM SKILLCODES 
                WHERE NAME = 'Python')
    OR SKILL_CODE & (SELECT CODE
                    FROM SKILLCODES 
                WHERE NAME ='C#')
ORDER BY ID;