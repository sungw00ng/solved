## 문제
https://solvesql.com/problems/daily-arppu/

```text
3단계였고 간단했다.
```

```sql
SELECT 
  DATE(d.order_purchase_timestamp) AS dt, -- 매출 날짜
  COUNT(DISTINCT d.customer_id) AS pu, -- 결제 고객 수
  ROUND(SUM(p.payment_value),2) AS revenue_daily, -- 해당 날짜의 매출액
  ROUND(
    SUM(p.payment_value)
    / 
    COUNT(DISTINCT d.customer_id),2) AS arppu -- 결제 고객 1인 당 평균 결제 금액 ARPPU
FROM olist_orders_dataset AS d 
JOIN olist_order_payments_dataset AS p
ON d.order_id=p.order_id
WHERE DATE(d.order_purchase_timestamp)>='2018-01-01'
GROUP BY DATE(d.order_purchase_timestamp)
ORDER BY dt ASC;
```
