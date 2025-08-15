SELECT 
p.product_id,
p.product_name,
SUM(p.price*o.amount) AS total_sales
FROM food_product AS p
JOIN food_order AS o
ON p.product_id=o.product_id
WHERE o.produce_date LIKE '2022-05%'
GROUP BY o.product_id
ORDER BY total_sales DESC,p.product_id;
