-- 사원별 성과금 정보
-- 평가 점수에 따른 평가 등급과 성과금
WITH S AS (
SELECT EMP_NO, SUM(SCORE)/2 AS SCORE
FROM HR_GRADE 
GROUP BY EMP_NO
),
G AS (
SELECT EMP_NO, CASE WHEN SCORE >= 96 THEN 'S'
            WHEN SCORE >= 90 THEN 'A'
            WHEN SCORE >= 80 THEN 'B'
            ELSE 'C' END AS GRADE
FROM S
)

SELECT EMP_NO, EMP_NAME, GRADE, CASE WHEN GRADE = 'S' THEN SAL*0.2
                                     WHEN GRADE = 'A' THEN SAL*0.15
                                     WHEN GRADE = 'B' THEN SAL*0.1
                                     ELSE 0 END AS BONUS
FROM HR_EMPLOYEES HE JOIN G USING(EMP_NO)
ORDER BY 1;












-- 평가 점수 조회하기
# SELECT EMP_NO, YEAR, AVG(SCORE), CASE WHEN AVG(SCORE) >= 96 THEN 'S'
#                     WHEN AVG(SCORE) >= 90 THEN 'A'
#                     WHEN AVG(SCORE) >= 80 THEN 'B'
#                     ELSE 'C' END AS GRADE
# FROM HR_GRADE 
# GROUP BY EMP_NO, YEAR;

-- 등급별 보너스
# SELECT A.EMP_NO, A.EMP_NAME, B.GRADE, CASE WHEN GRADE='S' THEN SAL*0.2
#                             WHEN GRADE='A' THEN SAL*0.15
#                             WHEN GRADE='B' THEN SAL*0.1
#                             ELSE 0 END AS BONUS
# FROM HR_EMPLOYEES A JOIN (SELECT EMP_NO, CASE WHEN AVG(SCORE) >= 96 THEN 'S'
#                     WHEN AVG(SCORE) >= 90 THEN 'A'
#                     WHEN AVG(SCORE) >= 80 THEN 'B'
#                     ELSE 'C' END AS GRADE
#                     FROM HR_GRADE 
#                     GROUP BY EMP_NO, YEAR) B USING(EMP_NO)
# ORDER BY 1;

-- 점수별 등급 구분
# CASE WHEN (SUM(SCORE)/2) >= 96 THEN 'S'
#                     WHEN (SUM(SCORE)/2) >= 90 THEN 'A'
#                     WHEN (SUM(SCORE)/2) >= 80 THEN 'B'
#                     ELSE 'C' END AS GRADE