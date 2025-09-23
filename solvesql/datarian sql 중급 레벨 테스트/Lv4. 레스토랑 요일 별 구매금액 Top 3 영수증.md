## Lv4. 레스토랑 요일 별 구매금액 Top 3 영수증
https://solvesql.com/problems/top-3-bill/

```text
서브쿼리와 기본적인 윈도우 함수를 활용하는 기본적인 문제였다.
예제 테이블이 하나라서 쉽게 풀 수 있었다.
```

```sql
SELECT
  day,
  time,
  sex,
  total_bill
FROM(
  SELECT
    *,
    DENSE_RANK() OVER(
      PARTITION BY t.day ORDER BY total_bill DESC) AS d
  FROM tips AS t
) AS noooo
WHERE d<=3;
```
