SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS 
WHERE (SELECT CODE
        FROM SKILLCODES 
        WHERE NAME = 'Python') = SKILL_CODE & (SELECT CODE
                                                FROM SKILLCODES 
                                                 WHERE NAME = 'Python')
OR (SELECT CODE
    FROM SKILLCODES 
    WHERE NAME = 'C#') = SKILL_CODE & (SELECT CODE
                                        FROM SKILLCODES 
                                        WHERE NAME = 'C#')
ORDER BY 1;