select
count(fish_type) as FISH_COUNT,
month(time) as MONTH
from fish_info
group by month(time)
order by month;
