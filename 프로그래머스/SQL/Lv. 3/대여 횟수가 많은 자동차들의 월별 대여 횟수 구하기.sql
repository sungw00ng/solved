SELECT
    MONTH(h.start_date) AS MONTH,
    h.car_id AS CAR_ID,
    count(*) AS RECORDS
FROM car_rental_company_rental_history AS h
 -- c: 대여기록 5회 이상 추출
JOIN (
    SELECT car_id
    FROM car_rental_company_rental_history
    WHERE DATE(start_date) BETWEEN '2022-08-01' AND '2022-10-31'
    GROUP BY car_id
    HAVING count(*)>=5
) AS c
ON h.car_id=c.car_id
WHERE DATE(start_date) BETWEEN '2022-08-01' AND '2022-10-31'
-- 3개월 대여기록 5회 이상(join) & 월별 car_id
GROUP BY MONTH,h.car_id
ORDER BY MONTH,h.car_id DESC;
