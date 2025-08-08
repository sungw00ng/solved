SELECT 
car_id,
    CASE
    WHEN car_id IN (
        SELECT car_id
        FROM car_rental_company_rental_history
        WHERE DATE('2022-10-16') BETWEEN DATE(start_date) AND DATE(end_date) 
        )
        THEN '대여중'
        ELSE '대여 가능'
    END AS AVAILABILITY
FROM car_rental_company_rental_history
GROUP BY car_id,AVAILABILITY
ORDER BY car_id DESC;
