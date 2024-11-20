# Write your MySQL query statement below

SELECT 
	query_name,
	ROUND(AVG(rating / position), 2) AS quality,
	ROUND(avg(CASE when rating < 3 then 1 else 0 End) * 100, 2) AS poor_query_percentage 

FROM 
	Queries
WHERE query_name is not null
GROUP BY 
	query_name
