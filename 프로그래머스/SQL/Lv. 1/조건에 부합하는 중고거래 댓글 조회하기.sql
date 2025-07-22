select
board.title as TITLE,
board.board_id as BOARD_ID,
reply.reply_id as REPLY_ID,
reply.writer_id as WRITER_ID,
reply.contents as CONTENT,
date_format(reply.created_date,'%Y-%m-%d') as CREATED_DATE
from 
used_goods_board as board
inner join used_goods_reply as reply
    on board.board_id=reply.board_id 
where substr(board.created_date,1,7)='2022-10'
order by reply.created_date,board.title
