# Write your MySQL query statement below

select email from 
(select count(email) as num_of_email,email
from Person
group by(email)) as T
where num_of_email>1