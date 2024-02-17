with step1 as (
select email, count(id) as c1
from person
group by email)

select email from step1 where c1>1