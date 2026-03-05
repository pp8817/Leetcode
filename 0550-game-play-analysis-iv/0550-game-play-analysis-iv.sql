SELECT 
    ROUND(
        COUNT(a0.player_id)/(SELECT COUNT(DISTINCT player_id) FROM Activity)
        ,2) AS 'fraction'
FROM Activity a0 JOIN (
    SELECT 
        player_id,
        MIN(event_date) AS first_date
    FROM Activity
    GROUP BY player_id
) a1 ON a0.player_id = a1.player_id
    AND a1.first_date = DATE_SUB(a0.event_date, INTERVAL 1 DAY);