SELECT
i.id,
n.fish_name,
i.length
FROM fish_info AS i
JOIN fish_name_info AS n
ON i.fish_type=n.fish_type
WHERE i.length= (
    SELECT MAX(length)
    FROM fish_info
    WHERE fish_type=i.fish_type
)
ORDER BY i.id;
