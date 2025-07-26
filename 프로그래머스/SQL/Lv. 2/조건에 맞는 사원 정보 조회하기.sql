select
sum(grade.score) as SCORE,
grade.emp_no as EMP_NO,
EMP.emp_name as EMP_NAME,
EMP.position as POSITION,
EMP.email as EMAIL
from hr_department as DM
join hr_employees as EMP
on DM.dept_id=EMP.dept_id
join hr_grade as grade
on EMP.emp_no=grade.emp_no
where grade.year=2022
group by EMP_NO,EMP_NAME,POSITION,EMAIL
order by SCORE desc
limit 1;
