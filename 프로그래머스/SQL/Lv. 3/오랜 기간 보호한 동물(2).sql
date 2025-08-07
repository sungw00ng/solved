SELECT
outs.animal_id AS ANIMAL_ID,
outs.name AS NAME
FROM animal_ins AS ins
RIGHT OUTER JOIN animal_outs AS outs  
ON ins.animal_id=outs.animal_id
ORDER BY DATEDIFF(outs.datetime,ins.datetime) DESC
LIMIT 2;
