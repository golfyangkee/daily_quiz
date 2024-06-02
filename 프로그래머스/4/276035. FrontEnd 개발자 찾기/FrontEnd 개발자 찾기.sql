-- front end 코드 알기
-- CATEGORY 가 FRONT END
-- javascript, react, vue
WITH FE AS (
SELECT *
FROM SKILLCODES 
WHERE CATEGORY = 'Front End'
),
-- 스킬코드가 맞는지
-- FE의 CODE랑 개발자가 SKILL_CODE랑 &했을 때 CODE랑 같으면
-- CODE들 중 하나라도 가지고 있으면 
-- CODE = CODE & SKILL_CODE
COR AS (
SELECT *
FROM DEVELOPERS D JOIN FE ON D.SKILL_CODE & FE.CODE = FE.CODE
)

-- 정답
-- JOIN을 사용하면 여러개의 스킬을 보유한 경우 중복발생
-- DISTINCT ID 를 여기서 하던 아니면 위에서 해야한다.
SELECT DISTINCT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM COR
ORDER BY ID;
