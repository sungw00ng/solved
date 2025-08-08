SELECT
dept.dept_id,
dept.dept_name_en,
ROUND(AVG(emp.sal)) AS AVG_SAL
FROM hr_department AS dept
JOIN hr_employees AS emp
ON dept.dept_id=emp.dept_id
GROUP BY dept.dept_id
ORDER BY AVG(emp.sal) desc;
