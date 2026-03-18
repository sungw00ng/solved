### 10308_Salaries Differences
https://platform.stratascratch.com/coding/10308-salaries-differences?code_type=3
```yml
Company : Linkedln, Dropbox
Difficulty : Easy
Question Type : 
Title : Salaries Differences
```

- My solution
```sql
/*
select department_id
from db_employee

select id
from db_dept;

1- engineering
4- marketing
*/
select max(val)-min(val)
from (
    select max(salary) as val
    from db_employee
    where department_id=1
    union all
    select max(salary)
    from db_employee
    where department_id=4 
) ab
```

- Analyze
```
in my opinion, i liked this user'n answer.
the answer is as follows:
```
```sql
---
christpb@usc.edu
SELECT 
ABS(MAX(CASE WHEN department = 'marketing' THEN salary end) -
MAX(CASE WHEN department = 'engineering' THEN salary end))
FROM db_employee
JOIN db_dept
ON db_employee.department_id = db_dept.id;
---
```
```
When I studied 'The Principle of the Optimizer',
I remember thinking that '~department_id=1 union all ~department_id=4' was more cost-effective than 'department_id in (1, 4)'.
But wasn't there a better way?
It's impressive that user 'christpb' figured out how to use Scala subqueries like that.
```
