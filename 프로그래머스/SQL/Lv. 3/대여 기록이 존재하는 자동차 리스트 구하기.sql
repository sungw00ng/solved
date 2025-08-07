SELECT DISTINCT h.car_id
FROM car_rental_company_car as c
JOIN car_rental_company_rental_history as h
ON c.car_id=h.car_id
where c.car_type='세단' and month(h.start_date)=10
order by car_id desc;
