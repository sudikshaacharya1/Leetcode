select E.name as Employee
from Employee E 
inner join Employee M
on m.id=e.managerid
where E.salary > m.salary