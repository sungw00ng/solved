SELECT
    ORDER_ID,
    PRODUCT_ID,
    DATE_FORMAT(out_date,'%Y-%m-%d') AS OUT_DATE,
    CASE
        WHEN DATE(out_date) <= '2022-05-01' THEN '출고완료'
        WHEN out_date IS NOT NULL THEN '출고대기'
        else '출고미정'
    end as 출고여부
FROM food_order 
ORDER BY order_id;
