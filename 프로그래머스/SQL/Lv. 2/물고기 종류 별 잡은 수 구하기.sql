select
count(*) as FISH_COUNT,
fish_name
from fish_info as f
join fish_name_info as n
on f.fish_type=n.fish_type
group by fish_name
order by FISH_COUNT desc
