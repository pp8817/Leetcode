SELECT d.name AS Department, t.name AS Employee, salary AS Salary
FROM (SELECT id, name, departmentId, salary, DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) as dr
FROM Employee) t JOIN Department d ON t.departmentId = d.id
WHERE t.dr<=3