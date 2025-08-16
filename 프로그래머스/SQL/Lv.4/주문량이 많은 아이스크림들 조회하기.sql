-- flavor
-- (7월 아이스크림 총 주문량)+(상반기 아이스크림 총 주문량) 기준, 상위 3개 맛 내림차순
SELECT hap.flavor
FROM (
    SELECT flavor,total_order FROM first_half
    UNION ALL
    SELECT flavor,total_order FROM JULY
) AS hap
GROUP BY hap.flavor
ORDER BY SUM(hap.total_order) DESC
LIMIT 3;
