SELECT a1.machine_id, ROUND(AVG(a1.timestamp - a0.timestamp), 3) AS processing_time
FROM Activity a1 JOIN Activity a0
    ON a1.machine_id = a0.machine_id 
        AND a1.process_id = a0.process_id
        AND a0.activity_type = 'start'
        AND a1.activity_type = 'end'
GROUP BY a1.machine_id