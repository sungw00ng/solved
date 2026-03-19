### 10299_Finding Updated Records
https://platform.stratascratch.com/coding/10308-salaries-differences?code_type=3
```yml
Company : Microsoft
Difficulty : Easy
Question Type : 
Title : Finding Updated Records
```

- My solution
```
Solution is incorrect.
When there are multiple maximum salaries,
I need to print only one, but i couldn't figure out how to do it right away.
I think this was the cause.
```
```sql
/*
1. You can consider the current salary for an employee is 
    the largest salary value among their records.
2. multiple records share the same maximum salary, 
return any one of them.
*/
select 
    id, 
    first_name,
    last_name,
    department_id,
    max(salary) as salary
from ms_employee_salary
group by 
    id,
    first_name,
    last_name,
    department_id
order by id;
```

- Analyze
```
As user pennyPincher1218 correctly pointed out,
let's add 'where rn=1' to the 'row_number' clause.
```
```sql
select 
    id,
    first_name,
    last_name,
    department_id,
    salary
from (
    select *,
        row_number() over (partition by id order by salary desc,
            department_id desc) as rn
    from ms_employee_salary
) as t
where rn=1;
```
