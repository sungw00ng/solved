-- sales_date,product_id,user_id(NULL포함),sales_amount
-- 2022년 3월의 온오프라인 상품 판매 데이터
-- *오프라인 user_id->NULL
SELECT 
DATE_FORMAT(a.sales_date,'%Y-%m-%d') AS SALES_DATE,
a.product_id,
a.user_id,
a.sales_amount
FROM (
SELECT sales_date,product_id,user_id,sales_amount
FROM online_sale
UNION
SELECT sales_date,product_id,NULL,sales_amount
FROM offline_sale
) AS a
WHERE DATE_FORMAT(a.sales_date,'%Y-%m-%d') BETWEEN '2022-03-01' AND '2022-03-31'
ORDER BY a.sales_date ASC, a.product_id ASC, a.user_id ASC;
