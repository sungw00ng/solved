WITH RECURSIVE timetable (hour) AS (
    SELECT 0 
    UNION
    SELECT hour+1 
    FROM timetable
    WHERE hour<23
)
SELECT 
hour, 
COUNT(a.animal_id)
FROM timetable AS t
LEFT JOIN animal_outs AS a
ON t.hour=HOUR(a.datetime)
GROUP BY hour
order by hour;
