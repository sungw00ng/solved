-- left outer join
SELECT ins.name,
ins.datetime
FROM animal_ins AS ins
LEFT JOIN animal_outs AS outs
ON ins.animal_id=outs.animal_id
-- A-B (IS NULL 필수)
WHERE outs.animal_id IS NULL
ORDER BY datetime
limit 3;
