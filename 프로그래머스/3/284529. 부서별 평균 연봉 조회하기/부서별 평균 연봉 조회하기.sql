SELECT HE.DEPT_ID, HD.DEPT_NAME_EN, ROUND(AVG(SAL)) AS AVG_SAL
FROM HR_EMPLOYEES HE JOIN HR_DEPARTMENT HD USING(DEPT_ID)
GROUP BY DEPT_ID
ORDER BY 3 DESC;