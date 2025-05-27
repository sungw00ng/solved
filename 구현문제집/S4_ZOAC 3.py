# 좌표를 반환하는 함수
def get_position(ch):
    for row_idx in range(3):
        if ch in layout[row_idx]:
            col_idx = layout[row_idx].index(ch)
            return (row_idx, col_idx)

# 쿼티 키보드 배열
layout = [
    ['z', 'x', 'c', 'v', 'b', 'n', 'm'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
]

# 시작 위치 입력
left_start, right_start = input().split()
text = input()

# 손 위치 초기화
hands = [get_position(left_start), get_position(right_start)]
sequence = [get_position(ch) for ch in text]

time = 0
for pos in sequence:
    row, col = pos
    # 오른손 영역 판단 조건
    if (row == 0 and col >= 4) or col >= 5:
        time += abs(hands[1][0] - row) + abs(hands[1][1] - col) + 1
        hands[1] = pos
    else:
        time += abs(hands[0][0] - row) + abs(hands[0][1] - col) + 1
        hands[0] = pos

print(time)
