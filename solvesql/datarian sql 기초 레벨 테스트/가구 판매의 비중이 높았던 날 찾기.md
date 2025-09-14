## 문제
https://solvesql.com/problems/day-of-furniture/ <br>

```text
난이도 4에 해당하는 문제였고, 문법 자체는 쉬운축에 속했다.
MYSQL로 풀이했을 때는 이게 왜 난이도 4인지 잘 이해가 되지 않았지만
SQLite는 furniture_pct를 만들 때 float형으로 캐스팅해줘야해서 +0.00을
붙여서 고평가받은 듯하다.
```

```sql
SELECT
  DATE(order_date) AS order_date,
  COUNT(DISTINCT CASE WHEN category='Furniture' THEN order_id END) AS furniture,
  ROUND(
    COUNT(DISTINCT CASE WHEN category='Furniture' THEN order_id END) 
    /
    COUNT(DISTINCT order_id)*100,2) AS furniture_pct
FROM records
GROUP BY order_date
HAVING COUNT(DISTINCT order_id)>=10
  AND furniture_pct>=40
ORDER BY furniture_pct DESC,order_date ASC;
```
