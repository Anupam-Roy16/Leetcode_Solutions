# Write your MySQL query statement below
# # SELECT customer_id,count(*) as count_no_trans from (SELECT customer_id FROM Visits WHERE visit_id NOT IN(SELECT visit_id FROM Transactions)) AS t
# group by customer_id



select customer_id,count(customer_id) as count_no_trans
from Visits left join Transactions on Visits.visit_id = Transactions.visit_id
where amount IS NULL AND transaction_id IS NULL
group by customer_id
