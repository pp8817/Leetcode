(SELECT u.name AS results
FROM MovieRating mr JOIN Users u ON u.user_id = mr.user_id
GROUP BY mr. user_id
ORDER BY COUNT(DISTINCT mr.movie_id) DESC, name ASC
LIMIT 1)

UNION ALL

(SELECT m.title AS results
FROM Movies m JOIN MovieRating mr ON m.movie_id = mr.movie_id
WHERE '2020-02-01' <= mr.created_at AND mr.created_at < '2020-03-01'
GROUP BY mr.movie_id
ORDER BY AVG(rating) DESC, m.title ASC
LIMIT 1)