SELECT s0.product_id, s1.first_year, s0.quantity, s0.price
FROM Sales s0 JOIN
    (SELECT product_id, MIN(YEAR) as first_year
    FROM Sales
    GROUP BY product_id
    ) s1 ON s0.product_id = s1.product_id AND s0.year = s1.first_year