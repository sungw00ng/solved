SELECT
a.id,
IFNULL(b.child_count,0) AS child_count 
FROM ecoli_data as a
-- B.child_count=null,1,2,1
LEFT JOIN (
    -- 1:1, 2:2, 4:1
    SELECT 
        parent_id,
        COUNT(*) AS child_count
    FROM ecoli_data
    WHERE parent_id IS NOT NULL
    GROUP BY parent_id
) AS b
ON a.id=b.parent_id
ORDER BY a.id;
