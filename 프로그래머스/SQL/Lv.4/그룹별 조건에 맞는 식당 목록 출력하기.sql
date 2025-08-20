-- member_name,review_text,review_date
SELECT
p.member_name,
r.review_text,
DATE_FORMAT(r.review_date,'%Y-%m-%d') AS REVIEW_DATE
FROM member_profile AS p
JOIN rest_review AS r
ON p.member_id=r.member_id
WHERE p.member_id=(
    SELECT member_id
    FROM rest_review
    GROUP BY member_id
    ORDER BY COUNT(*) DESC
    LIMIT 1
)
ORDER BY REVIEW_DATE ASC,r.review_text ASC;
