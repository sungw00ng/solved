SELECT
    c.car_id,
    c.car_type,
    -- FEE(INT):round(...*(1-discount_rate/100),0)
    round(30*c.daily_fee*(1-p.discount_rate/100),0) AS FEE
FROM car_rental_company_car AS c
JOIN car_rental_company_discount_plan AS p
ON c.car_type=p.car_type
-- 자동차 종류가 '세단' 또는 'SUV'인 자동차
WHERE (c.car_type='세단' OR c.car_type='SUV') 
    
    AND p.duration_type LIKE '30일%'
    
    -- 11월 1일부터 2022 11월 30일까지 대여가능한 자동차
    -- 이 기간에 아무도 대여하지 않은 자동차
    AND car_id NOT IN (
        SELECT car_id
        FROM car_rental_company_rental_history AS h
        -- 11월과 무조건 겹치는 경우
        WHERE h.end_date>='2022-11-01' 
        AND h.start_date<='2022-11-30'
    )
    
    -- 50만원 이상 200만원 미만
    AND 
    round(30*c.daily_fee*(1-p.discount_rate/100),0)>=500000 
    AND 
    round(30*c.daily_fee*(1-p.discount_rate/100),0)<2000000
ORDER BY FEE DESC,c.car_type ASC,c.car_id DESC;
