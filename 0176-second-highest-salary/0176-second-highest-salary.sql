SELECT MAX(salary) AS SecondHighestSalary
FROM (
    SELECT id, salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rn
    FROM Employee) t
WHERE rn = 2