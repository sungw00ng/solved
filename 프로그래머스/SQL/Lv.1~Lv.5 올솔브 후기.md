# LV.1
- DB 유형을 처음 풀어봤는데 쉽고 간단하니 재밌었다.
- 아래 4문제 정도만 즐겨찾기 해놓고, 복습할 때 보면 될 듯하다.

>[과일로 만든 아이스크림 고르기](https://school.programmers.co.kr/learn/courses/30/lessons/133025) <br>
>[자동차 대여 기록에서 장기/단기 대여 구분하기](https://school.programmers.co.kr/learn/courses/30/lessons/151138) <br>
>[조건에 부합하는 중고거래 댓글 조회하기](https://school.programmers.co.kr/learn/courses/30/lessons/164673) <br>
>[특정 형질을 가지는 대장균 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/301646) <br>

<br>

# Lv.2
- 8월 5일 Lv. 2를 부셨다... Lv.2 중반쯤부터 난이도가 천천히 상승하다가 후반부에 급상승했다..
- `Lv. 1 올솔 후기`와 마찬가지로 정리를 해두려고 한다.

<br>

### order by case when end  <br>
- join on, case when end 등을 기본적으로 개념을 안다는 느낌에서 베이스로 깔고 문제를 푸는 느낌이었다. <br>
- 다만 아래문제에서 case when end를 order by에도 사용할 수 있다는 사실에 처음에 꽤 충격먹었던 것 같다.. <br>
[고양이와 개는 몇 마리 있을까](https://school.programmers.co.kr/learn/courses/30/lessons/59040)<br>

<br>

### group by, having <br>
- group by, having에 대한 구체적인 응용법을 익힐 수 있었다. <br>
- having 절이 까다로운 문제 몇몇이 있었다. <br>

<br>

### subquery <br>
- 서브쿼리가 들어간 문제들이 있었는데... 어려웠다. <br>
- select, from, where 구분없이 어디 어디서나 곳곳에 서브쿼리를 써야하는 유형들이 있었는데 <br>
- 왜 해당하는 라인에 서브쿼리를 써야하는지에 대한 개념적인 원리를 떠올리는데 많은 시간이 들었다. <br>
- 예를 들어, 아래 문제같은 경우 select 외에 where에도 서브쿼리를 달아서 푸는것이 가능했다. <br>
[업그레이드 된 아이템 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/273711)<br>

<br>

### bit flag <br>
- Lv. 2에서 `부모의 형질을 모두 가지는 대장균 찾기`가 정답률이 가장 낮은 문제였는데, <br>
- 하나의 테이블을 join on으로 두 개로 늘려서 where 절에 사용해야하는 창의적인 문제였다. <br>
- 복잡도가 높진 않아서 이정도면...뭐 풀만하다라고 느꼈던 것 같다. <br>
[부모의 형질을 모두 가지는 대장균 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/301647)<br>
- 실질적으로는 같은 bit flag 문제 중에 `조건에 맞는 개발자 찾기`가 더 어려웠다. <br>
- 코드 스킬을 더하기 하는데 이게 왜 bit flag를 쓰는 문제인거지..? 하고 혼동이 왔었고 <br>
- from에 서브쿼리로 두개의 테이블을 하나로 합쳐야하는... 다소 해결법을 떠올리기 어려웠다고 느꼈다. <br>
[조건에 맞는 개발자 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/276034)<br>

<br>

### CTE
[연도별 대장균 크기의 편차 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/299310)<br>
- 그냥 구현 자체를 떠올리지 못했던 것 같다.
- 답지를 보면 from에 서브쿼리를 달아서 푸는 유형이 하나 있고,
- 또 다른 유형으로 CTE (Common Table Expression)라고 하여
- 테이블 쿼리를 통해 만들어낸 임시적인 데이터 세트 `with as` 구문을 select 앞에 달아서
- 푸는 방법 등등 2가지가 있는데 앞선 유형은 떠올리기 힘들고,
- 그나마 두번째 유형은 새로운 문법이라 개념을 이해하기 어려웠다.
- 많은 반복적인 풀이를 하면서 개념을 이해할 필요가 있다고 생각한다.
- GROUP BY [조건에 맞는 사원 정보 조회하기](https://school.programmers.co.kr/learn/courses/30/lessons/284527)<br>
- String, Date [자동차 평균 대여 기간 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/157342)<br>

# Lv.3
- Join이나 서브쿼리를 써야되는 타이밍에 대해 이제 어느정도 감을 익혔다.
- 체감상 LV.2 처음 익혔을 때보단 쉬웠다.
- `단일 행 함수`나 `윈도우 함수`에 대해 공부를 더 해야할 것 같다.
>[조건에 맞는 사용자 정보 조회하기](https://school.programmers.co.kr/learn/courses/30/lessons/164670) <br>
>[특정 조건을 만족하는 물고기별 수와 최대 길이 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/298519) <br>
>[대장균의 크기에 따라 분류하기 2](https://school.programmers.co.kr/learn/courses/30/lessons/301649) <br>

<br>

# Lv.4
- 이쯤 되니까 CTE를 사용하는 것이 두렵지 않다. 하지만 가능하면 피하려고 했다 ㅋㅋㅋ
- FEE를 구하는 `(1-percent)/100` 을 떠올려야 하는 신유형이 있었는데 이 부분은 답지를 오랫동안 참고했던 것 같다.
- 재귀형 문제는 WITH RECURSIVE 뷰이름 AS를 무조건 써야하는데 이해하는 것에 꽤 긴 시간을 들였다.
- 문법적인 난이도가 더 상승하지 않지만, 문제의 독해력이 필요한 레벨이었다.

<br>

# Lv.5
- 대장균 찾기는, 재귀형 문제라서 넘어가고,
- `상품을 구매한 회원 비율 구하기`같은 경우, 지엽적으로 필요하지 않는 지문을 피해서 읽을 수 없었다.
- 즉, 이 문제의 지문은 꽤 신중히 읽어야 했는데 `2021년 가입회원 중 연,월별 구매 회원 수/2021년 전체 회원 수`를 예시로 들면,
- 2021년에 가입했으나, 2022년에도 쇼핑몰 물건을 구매할 수 있음에 유의하여 풀어야 했다.

<br>


### 그래서..
```text
솔직히 말하면, 이 과정을 모두 푼다고 해서 관련 데이터자격 시험을 합격할 수 있다는 보장은 없다고 생각한다.
하지만 SQL을 읽고 이해하는 능력이 눈에 띄게 향상된다는 점에서 큰 성취감을 느꼈다.
2단계를 꾸준히 파고들어 임계점을 돌파하고 나니, 3단계 이후의 문제들도 훨씬 수월하게 접근할 수 있었다.
비록 내가 데이터 엔지니어나 데이터 분석가가 되려는 것은 아니지만,
실제 데이터를 활용해 문제를 해결해야 하는 프로젝트나 테스트에서는 충분히 도움이 될 것 같다.
```
