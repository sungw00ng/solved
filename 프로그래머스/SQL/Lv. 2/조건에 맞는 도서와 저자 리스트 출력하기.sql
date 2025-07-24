select
b.book_id,
a.author_name,
date_format(b.published_date,'%Y-%m-%d') as PUBLISHED_DATE
from book as b
inner join author as a
on b.author_id=a.author_id
where b.category='경제'
order by b.published_date
