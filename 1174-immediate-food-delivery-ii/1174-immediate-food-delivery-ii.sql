SELECT 
    ROUND(
        SUM(d0.customer_pref_delivery_date=d0.order_date)*100/COUNT(*)
    , 2) AS immediate_percentage
FROM (
    SELECT 
    delivery_id,
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date ASC) AS rn
    FROM Delivery) d1 JOIN Delivery d0 ON d1.delivery_id = d0.delivery_id
WHERE rn = 1;