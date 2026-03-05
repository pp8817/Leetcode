SELECT customer_id
FROM (
    SELECT customer_id, COUNT(DISTINCT product_key) as cnt
    FROM Customer
    GROUP BY customer_id
) c
WHERE cnt = (SELECT COUNT(*) FROM Product)