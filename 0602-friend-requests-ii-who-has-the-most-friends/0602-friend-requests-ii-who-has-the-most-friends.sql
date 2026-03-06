SELECT id, SUM(cnt1) as num
FROM (
    (SELECT requester_id as id, COUNT(*) AS cnt1
    FROM RequestAccepted
    GROUP BY requester_id)

    UNION ALL

    (SELECT accepter_id as id, COUNT(*) AS cnt1
    FROM RequestAccepted
    GROUP BY accepter_id)
    ) t
GROUP BY id
ORDER BY num DESC
LIMIT 1;
