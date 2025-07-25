select
p.product_code,
sum(p.price*s.sales_amount) as SALES
from product as p
inner join offline_sale as s
on p.product_id=s.product_id
group by p.product_code 
order by SALES desc,p.product_code asc
