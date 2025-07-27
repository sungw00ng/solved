select
count(*) as FISH_COUNT
from fish_info as f
join fish_name_info as name
on f.fish_type=name.fish_type
where name.fish_name='BASS' or name.fish_name='SNAPPER'
