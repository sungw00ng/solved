select fh.flavor
from first_half as fh
join icecream_info as info
on fh.flavor=info.flavor
where fh.total_order>3000 
and info.ingredient_type='fruit_based'
order by fh.total_order desc
