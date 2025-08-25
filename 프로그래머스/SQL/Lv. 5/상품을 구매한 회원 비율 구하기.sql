SELECT
    YEAR(s.sales_date) AS year,
    MONTH(s.sales_date) AS month,
    COUNT(DISTINCT i.user_id) AS purchased_users,
    -- 2021년 가입한 회원 중 상품을 구매한 회원/2021년에 가입한 전체 회원
    ROUND(
        COUNT(DISTINCT i.user_id) /
        (
        SELECT COUNT(DISTINCT user_id) 
        FROM user_info
        WHERE YEAR(joined)=2021
        )
    ,1) AS puchased_ratio
FROM user_info AS i
JOIN online_sale AS s
ON i.user_id=s.user_id
WHERE YEAR(i.joined)=2021
GROUP BY year,month
ORDER BY year,month;
