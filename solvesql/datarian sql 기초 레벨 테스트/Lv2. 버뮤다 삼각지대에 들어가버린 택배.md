## 문제
https://solvesql.com/problems/shipment-in-bermuda/ <br>

```text
2단계라 표시되어있는데, 이상하게 3단계스러운 문제..
문법적인 난이도는 낮았으나
역시나 실무형 쿼리는 낯설다.
```



```sql
SELECT
-- 2017년 1월 한 달 동안 택배사에 전달되었지만 배송 완료는 되지 않은 주문 건수
-- 주문이 없었던 날은 출력에서 제외해주세요.
DATE(order_delivered_carrier_date) AS delivered_carrier_date,
COUNT(order_id) AS orders
-- 택배사 도착일을 기준으로 집계하는 쿼리를 작성해주세요.
FROM olist_orders_dataset
WHERE order_delivered_carrier_date LIKE '2017-01%'
AND order_delivered_customer_date IS NULL
GROUP BY DATE(order_delivered_carrier_date)
-- 택배사 도착일 기준 오름차순
ORDER BY order_delivered_carrier_date ASC;
```
