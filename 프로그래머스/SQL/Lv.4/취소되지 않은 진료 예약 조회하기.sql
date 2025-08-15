-- 2022년 4월 13일 취소되지 않는 CS 진료 예약 내역 조회
SELECT
a.apnt_no,
p.pt_name,
p.pt_no,
a.mcdp_cd,
d.dr_name,
a.apnt_ymd

FROM appointment AS a 
-- mddr_id=dr_id
JOIN doctor AS d ON a.mddr_id=d.dr_id
JOIN patient AS p ON a.pt_no=p.pt_no
WHERE a.mcdp_cd='CS' 
AND DATE(a.apnt_ymd)='2022-04-13'
AND a.apnt_cncl_yn='N'

-- 진료예약일시 오름차순
ORDER BY a.apnt_ymd;
