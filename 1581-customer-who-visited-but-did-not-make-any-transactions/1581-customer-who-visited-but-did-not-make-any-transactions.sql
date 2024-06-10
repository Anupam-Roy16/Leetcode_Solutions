# Write your MySQL query statement below
SELECT customer_id,count(*) as count_no_trans from (SELECT customer_id FROM Visits WHERE visit_id NOT IN(SELECT visit_id FROM Transactions)) AS t
group by customer_id