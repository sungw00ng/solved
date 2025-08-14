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
