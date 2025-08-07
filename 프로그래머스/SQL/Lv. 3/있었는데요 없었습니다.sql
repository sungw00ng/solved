SELECT
outs.animal_id AS ANIMAL_ID,
outs.name AS NAME
FROM animal_ins AS ins
JOIN animal_outs AS outs
ON ins.animal_id=outs.animal_id
WHERE ins.datetime>outs.datetime
ORDER BY ins.datetime;
