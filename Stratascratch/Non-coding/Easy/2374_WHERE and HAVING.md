### 2374_WHERE and HAVING
https://platform.stratascratch.com/technical/2374-where-and-having
```yml
Company : Spotify
Difficulty : Easy
Question Type : Technical
Title : WHERE and HAVING
```

- My solution
```
If i want to use Aggregate function in WHERE clause,  
This can serve as a good example of how to use the "HAVING" clause.
but "WHERE" clause don't use Aggregate function. 
```

- Analyze
```
1. why not?
: Aggregate functions cannot be used in the WHERE clause because aggregation happens after rows are filtered by WHERE.
2. Why isn't there an explanation of the SQL execution order?
: in SQL's logical execution order, the WHERE clause is evaluated before GROUPBYand aggregation functions.
3. The alternative explanation is weak.
: To filter results based on aggregates values, we should use the HAVING clause,
which is evaluated after GROUP BY.

Aggregate functions cannot be used in the WHERE clause because WHERE is evaluated before aggregation in SQL's logical execution order.
if we want to filter based on on aggregated results,
we should use the HAVING clause, which is evaluated after GROUP BY.

```
