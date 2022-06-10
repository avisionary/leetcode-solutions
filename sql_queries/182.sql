# Write your MySQL query statement below
select a.email
from person a
group by a.email
having count(email) > 1
