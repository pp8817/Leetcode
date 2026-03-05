SELECT person_name
FROM (
    SELECT *, SUM(weight) OVER(ORDER BY turn) as sum_weight
    FROM Queue
    ORDER BY turn DESC
    ) t
WHERE sum_weight <= 1000
LIMIT 1;