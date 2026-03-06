SELECT visited_on, amount, ROUND((amount/7), 2) as average_amount
FROM (
    SELECT 
        visited_on, 
        SUM(sum_amount) OVER (ORDER BY visited_on ASC ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as amount
    FROM (
        SELECT visited_on, SUM(amount) as sum_amount
        FROM Customer
        GROUP BY visited_on
        ) t
) t
WHERE DATE_ADD((SELECT MIN(visited_on) FROM Customer), INTERVAL 6 DAY) <= visited_on