SELECT 
    ROUND(
        SUM(customer_pref_delivery_date = order_date) * 100.0 / COUNT(*)
    , 2) AS immediate_percentage
FROM (
    SELECT
        order_date,
        customer_pref_delivery_date,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY order_date
        ) AS rn
    FROM Delivery
) t
WHERE rn = 1;