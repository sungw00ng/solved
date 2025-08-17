SELECT
-- 사원별 성과금 정보 조회 
-- 2017002 정호식 B 6500000
-- 2018001 김민석 B 6000000
-- emp_no,emp_name,grade[평가등급컬럼명],bonus[성과금컬럼명]
e.emp_no,
e.emp_name,
CASE     
    WHEN AVG(g.score)>=96 THEN 'S'
    WHEN AVG(g.score)>=90 THEN 'A'
    WHEN AVG(g.score)>=80 THEN 'B'
    ELSE 'C'
END AS grade,
CASE
    WHEN AVG(g.score) >= 96 THEN e.sal*0.2
    WHEN AVG(g.score) >= 90 THEN e.sal*0.15
    WHEN AVG(g.score) >= 80 THEN e.sal*0.1
    ELSE 0
END AS bonus
FROM hr_employees AS e
JOIN hr_department AS d ON e.dept_id=d.dept_id
JOIN hr_grade AS g ON e.emp_no=g.emp_no
GROUP BY e.emp_no,e.emp_name
ORDER BY emp_no;
