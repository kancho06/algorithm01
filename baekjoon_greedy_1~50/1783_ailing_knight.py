# 문제
# 병든 나이트가 N × M 크기 체스판의 가장 왼쪽아래 칸에 위치해 있다. 병든 나이트는 건강한 보통 체스의 나이트와 다르게 4가지로만 움직일 수 있다.
# 2칸 위로, 1칸 오른쪽
# 1칸 위로, 2칸 오른쪽
# 1칸 아래로, 2칸 오른쪽
# 2칸 아래로, 1칸 오른쪽
# 병든 나이트는 여행을 시작하려고 하고, 여행을 하면서 방문한 칸의 수를 최대로 하려고 한다.
# 병든 나이트의 이동 횟수가 4번보다 적지 않다면, 이동 방법을 모두 한 번씩 사용해야 한다.
# 이동 횟수가 4번보다 적은 경우(방문한 칸이 5개 미만)에는 이동 방법에 대한 제약이 없다.
# 체스판의 크기가 주어졌을 때, 병든 나이트가 여행에서 방문할 수 있는 칸의 최대 개수를 구해보자.
#
# 입력
# 첫째 줄에 체스판의 세로 길이 N와 가로 길이 M이 주어진다. N과 M은 2,000,000,000보다 작거나 같은 자연수이다.
#
# 출력
# 병든 나이트가 여행에서 방문할 수 있는 칸의 개수중 최댓값을 출력한다.

n, m = map(int, input().split())

if n == 1:      # 세로가 1 일때는 원점에서 이동하지 못함
    print(1)
elif n == 2:        # 세로가 2 일때는 1번 4번 방법이 불가능하니 4가지 방법을 다 쓸 수 없음으로 최대 이동횟수는 4가 된다
    print(min(4, ((m + 1) // 2)))
else:
    if m <= 6:      # 가로가 6이하라면 최대 이동횟수는 4이다.
        print(min(4, m))
    else:       # 가로가 7 이상이라면 오른쪽으로 두번가는 2, 3 번 방법을 한번씩만 써야 최대값이므로 가로 -2 를하여 최댓값을 구한다.
        print(m - 2)
