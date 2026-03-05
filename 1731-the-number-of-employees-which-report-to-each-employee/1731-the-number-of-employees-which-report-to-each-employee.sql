SELECT e0.employee_id, e0.name, e1.reports_count, e1.average_age
FROM Employees e0 JOIN (
    SELECT reports_to, COUNT(*) AS reports_count, ROUND(AVG(age)) AS average_age
    FROM Employees
    WHERE reports_to IS NOT NULL
    GROUP BY reports_to
) e1 ON e0.employee_id = e1.reports_to
ORDER BY employee_id ASC;