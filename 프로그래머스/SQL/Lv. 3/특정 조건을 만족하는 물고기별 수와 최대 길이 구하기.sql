SELECT
COUNT(*) AS fish_count,
MAX(length) AS max_length,
fish_type
FROM fish_info
GROUP BY fish_type
HAVING AVG(IF(IFNULL(length,0)<=10,10,length))>=33
ORDER BY fish_type
