select 
animal_type as ANIMAL_TYPE,
count(*) as count
from animal_ins
where animal_type='Cat' or animal_type='Dog'
group by animal_type
order by case animal_type
    when 'Cat' then 1
    when 'Dog' then 2
    end;
