SELECT
main.food_type,
main.rest_id,
main.rest_name,
main.favorites
FROM rest_info AS main 
JOIN (
    SELECT 
        food_type,
        MAX(favorites) AS mF
    FROM 
        rest_info
    GROUP BY 
        food_type
) AS sub
ON main.food_type=sub.food_type AND main.favorites=sub.mF
ORDER BY main.food_type desc;
