SELECT
a3.id
FROM ecoli_data AS a1
JOIN ecoli_data AS a2 ON a1.id=a2.parent_id
JOIN ecoli_data AS a3 ON a2.id=a3.parent_id
WHERE a1.parent_id IS NULL
ORDER BY a3.id;
