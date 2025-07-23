select 
animal_id as ANIMAL_ID,
name as NAME
from animal_ins
where name like '%el%' and animal_type='dog'
order by name;
