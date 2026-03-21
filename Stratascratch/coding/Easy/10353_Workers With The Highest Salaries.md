### 10353_Workers With The Highest Salaries
https://platform.stratascratch.com/coding/10353-workers-with-the-highest-salaries?code_type=3
```yml
Company : Amazon, DoorDash
Difficulty : Easy
Question Type : 
Title : Workers With The Highest Salaries
```

- My solution
```
Solved.
```
```sql
select
    t.worker_title
from worker w
join title t on w.worker_id=t.worker_ref_id
where w.salary=(select max(salary)
                from worker w
                join title t on worker_id=worker_ref_id
)
```

- Analyze
```
Claude AI said: “If the number exceeds 1 million,
the performance difference will be 2 to 5 times greater.”
It seems the subquery issue is the biggest problem.
The improvements are as follows:
```
```sql
SELECT t.worker_title
FROM worker AS w
INNER JOIN title AS t ON w.worker_id = t.worker_ref_id
WHERE w.salary = (
    SELECT MAX(salary)
    FROM worker
    WHERE EXISTS (SELECT 1 FROM title WHERE worker_ref_id = worker_id)
);
```
