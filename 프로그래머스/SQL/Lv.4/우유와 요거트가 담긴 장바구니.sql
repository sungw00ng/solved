-- cart_id
SELECT cart_id
FROM cart_products
WHERE name IN ("Yogurt","Milk")
GROUP BY cart_id
HAVING COUNT(DISTINCT name)=2
ORDER BY cart_id;
