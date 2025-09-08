## 문제
https://solvesql.com/problems/tip-analysis/

- 난이도 2에 해당하는 문제로 금방금방 풀 수 있었다.
  
```sql
SELECT 
day,
time,
ROUND(AVG(tip),2) AS avg_tip, 
ROUND(AVG(size),2) AS avg_size
FROM tips
GROUP BY day,time
ORDER BY day,time;
```
