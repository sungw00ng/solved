SELECT
CONCAT('/home/grep/src/',board_id,'/',file.file_id,file.file_name,file.file_ext) AS FILE_PATH
FROM used_goods_file AS file
WHERE board_id = (
    SELECT board_id
    FROM used_goods_board
    ORDER BY views DESC
    limit 1
)
ORDER BY file.file_id DESC;
