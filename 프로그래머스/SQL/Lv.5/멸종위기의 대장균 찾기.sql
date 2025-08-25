With RECURSIVE tier AS (
    SELECT
        id,
        parent_id,
        1 AS gene
    FROM
        ecoli_data
    WHERE
        parent_id IS NULL
    
    UNION ALL
    
    SELECT
        a.id,
        a.parent_id,
        gene+1 AS gene
    FROM
        -- cross(부모,자식 필터링)
        ecoli_data AS a, tier AS b
    WHERE
        b.id=a.parent_id
)
    
SELECT COUNT(*) AS COUNT,
a.gene AS generation
FROM tier AS a LEFT JOIN tier AS b ON a.id=b.parent_id
WHERE b.id IS NULL
GROUP BY a.gene
ORDER BY a.gene
