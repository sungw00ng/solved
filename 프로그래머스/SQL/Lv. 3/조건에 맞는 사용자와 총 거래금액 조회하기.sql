SELECT
b.user_id,
b.nickname,
SUM(price) as TOTAL_SALES
FROM used_goods_board AS a
JOIN used_goods_user as b
ON a.writer_id=b.user_id
WHERE STATUS='DONE'
GROUP BY b.user_id,b.nickname
HAVING SUM(price)>=700000
ORDER BY total_sales
