# Write your MySQL query statement belows
with data as (
select num,  
lead(num,1) over() as num1, 
lead(num,2) over() as num2
from logs)

select distinct(num) as ConsecutiveNums
from data where num=num2
and num=num1;