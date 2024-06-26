# Write your MySQL query statement below
(SELECT name AS results
FROM MovieRating JOIN Users ON MovieRating.user_id = Users.user_id
GROUP BY name
ORDER BY COUNT(*) DESC, name
LIMIT 1)

UNION ALL

(SELECT title AS results
FROM MovieRating JOIN Movies ON MovieRating.movie_id = Movies.movie_id
where created_at LIKE '2020-02-__'
GROUP BY title
ORDER BY AVG(rating) DESC, title

LIMIT 1);


