select 
product_id as PRODUCT_ID,
product_name as PRODUCT_NAME,
product_cd as PRODUCT_CD,
category as CATEGORY,
price as PRICE
from food_product
order by price desc
limit 1;
