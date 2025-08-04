select
info.item_id,
info.item_name,
info.rarity
from item_info as info
join item_tree as tree
on info.item_id=tree.item_id
where tree.parent_item_id in (
    select item_id
    from item_info
    where rarity='rare'
)

order by item_id desc;
