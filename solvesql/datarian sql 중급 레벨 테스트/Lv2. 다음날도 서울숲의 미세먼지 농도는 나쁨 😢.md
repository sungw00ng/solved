## 다음날도 서울숲의 미세먼지 농도는 나쁨 😢
https://solvesql.com/problems/bad-finedust-measure/

### 후기
```text
주어진 테이블도 1개였고, 자신 테이블을 참조하는 테이블 문제는 흔하니
난이도가 괜찮았다.
그런데, '-1 day' 키워드가 생각이 잘 안 떠올라서 조금 헤맸던 것 같다.
```

```sql
SELECT 
  m1.measured_at AS today,
  m2.measured_at AS next_day,
  m1.pm10,
  m2.pm10 AS next_pm10
FROM measurements AS m1
JOIN measurements AS m2
ON m1.measured_at=DATE(m2.measured_at,'-1 day')
WHERE m1.pm10<m2.pm10
```
