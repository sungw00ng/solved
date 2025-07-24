select
ingredient_type,
sum(total_order) as TOTAL_ORDER 
from first_half as f
inner join icecream_info as i
on f.flavor=i.flavor
group by i.ingredient_type
order by TOTAL_ORDER
