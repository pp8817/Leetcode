SELECT w0.id
FROM Weather w1
    JOIN Weather w0
    ON w1.recordDate = DATE_SUB(w0.recordDate, INTERVAL 1 DAY)
WHERE w0.temperature > w1.temperature;