### 2354_Common Table Expression
https://platform.stratascratch.com/technical/2354-common-table-expression
```yml
Company : Spotify
Difficulty : Easy
Question Type : Technical
Title : Common Table Expression
```

- My solution
```
CTE is a table containing dummy data.
The `with ~ as` clause uses values retrieved from the `FROM` clause of the main query, even though those values do not actually exist.
Its main advantage seems to have been the speed of the optimization process.
I think I mainly used it when writing hierarchical SQL queries.
```

- Analyze
```
It looks like I just need to polish the content a bit.

CTE is a temporary result set defined using the WITH clause.
It is mainly used to improve query readability, reuse intermediate results, and handle hierarchical queries using recursion.
```
