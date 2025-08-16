SELECT
-- year,month,gender,users
-- 년,월,성별 별로 상품을 구매한 회원수를 집계
YEAR(s.sales_date) AS year,
MONTH(s.sales_date) AS month,
i.gender AS gender,
COUNT(DISTINCT s.user_id)
FROM user_info AS i
JOIN online_sale AS s ON i.user_id=s.user_id
--  성별 정보가 없는 경우 결과에서 제외
WHERE i.GENDER IS NOT NULL
GROUP BY year,month,gender
ORDER BY year,month,gender
