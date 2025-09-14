## 문제
https://solvesql.com/problems/restaurant-vip/

```sql
-- 요일별로 가장 높은 금액의 결제 내역을 출력
SELECT 
total_bill,
tip,
sex,
smoker,
day,
time,
size
FROM tips AS t
WHERE total_bill=(
  SELECT MAX(total_bill)
  FROM tips
  WHERE day=t.day
);
```
