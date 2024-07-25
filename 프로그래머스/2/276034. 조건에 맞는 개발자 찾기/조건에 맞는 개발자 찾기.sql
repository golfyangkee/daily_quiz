SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS
WHERE SKILL_CODE & ((SELECT CODE
                    FROM SKILLCODES 
                    WHERE NAME = 'C#') + 
                    (SELECT CODE
                    FROM SKILLCODES 
                    WHERE NAME = 'Python'))!=0
ORDER BY 1;