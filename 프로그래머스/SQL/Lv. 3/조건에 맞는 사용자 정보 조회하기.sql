SELECT
u.user_id,
u.nickname,
CONCAT(u.city,' ',u.street_address1,' ',u.street_address2) AS '전체주소',
CONCAT(
    SUBSTR(u.tlno,1,3),
    '-',
    SUBSTR(u.tlno,4,4),
    '-',
    SUBSTR(u.tlno,8,4)
    ) AS '전화번호'
FROM used_goods_board AS b
JOIN used_goods_user AS u
ON b.writer_id=u.user_id
GROUP BY writer_id
HAVING COUNT(contents)>=3
ORDER BY u.user_id DESC;
