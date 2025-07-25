select
info.item_id,
info.item_name
from item_info as info
join item_tree as tree
on info.item_id=tree.item_id
where tree.parent_item_id is null
order by info.item_id
