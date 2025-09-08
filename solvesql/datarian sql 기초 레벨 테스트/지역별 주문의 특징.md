## 문제
https://solvesql.com/problems/characteristics-of-orders/


좀 당황했던 문제다. <br>
난이도 3에 해당하는 문제고 문법 자체는 쉬운 편이었지만, <br>
직접 테이블을 보면서 문제를 풀어나가야하는 약간 지엽적인 문제였기 때문이다. <br>
그리고, region, category 별 주문량을 계산해서 출력해야했기에 <br>
GROUP BY에 category 껴야 하나..?` 했는데 아니었다. <br>
풀이가 오래 걸리진 않았다. <br>

```sql
SELECT
region AS Region,
COUNT(DISTINCT(CASE WHEN category='Furniture' THEN order_id END)) AS 'Furniture',
COUNT(DISTINCT(CASE WHEN category='Office Supplies' THEN order_id end)) AS 'Office Supplies',
COUNT(DISTINCT(CASE WHEN category='Technology' THEN order_id END)) AS 'Technology'
FROM records
GROUP BY region
ORDER BY region ASC;
```
