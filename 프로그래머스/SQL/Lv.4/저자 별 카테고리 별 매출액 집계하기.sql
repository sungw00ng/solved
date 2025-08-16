SELECT
b.author_id,
a.author_name,
b.category,
SUM(b.price*s.sales) AS TOTAL_SALES
FROM book AS b
JOIN author AS a ON b.author_id=a.author_id
JOIN book_sales AS s ON b.book_id=s.book_id
WHERE s.sales_date LIKE '2022-01%'
GROUP BY b.author_id,a.author_name,b.category
ORDER BY b.author_id,b.category DESC;
