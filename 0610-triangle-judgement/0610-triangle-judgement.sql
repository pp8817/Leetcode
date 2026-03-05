SELECT x, y, z,
    CASE
        WHEN cnt = 1 THEN 'Yes' ELSE 'No'
    END AS triangle
FROM (
    SELECT 
        CASE
            WHEN x + y > z AND x + z > y AND z + y > x THEN 1 ELSE 0
        END AS cnt, x, y, z
    FROM Triangle
) t