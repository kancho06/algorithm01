# 문제
# 0과 1로만 이루어진 행렬 A와 행렬 B가 있다.
# 이때, 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하는 프로그램을 작성하시오.
#
# 행렬을 변환하는 연산은 어떤 3×3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 → 1, 1 → 0)
#
# 입력
# 첫째 줄에 행렬의 크기 N M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다.
# 둘째 줄부터 N개의 줄에는 행렬 A가 주어지고, 그 다음줄부터 N개의 줄에는 행렬 B가 주어진다.
#
# 출력
# 첫째 줄에 문제의 정답을 출력한다. 만약 A를 B로 바꿀 수 없다면 -1을 출력한다.

import sys

n, m = map(int, sys.stdin.readline().split())
a = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
b = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
result = 0


def flip(i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            a[x][y] = 1 - a[x][y]


# 예를들어 6 x 6 이 나왓을 때는 한칸이동해서 3x3 타일을 볼수 잇는 횟수가 총 4x4= 16번이다
# 5 x 5 가 나왓을 때는 한칸이동해서 3x3 타일을 볼수 잇는 횟수가  총 3 x 3 = 9번이 된다
# 그러므로 n, m 에 -2 를 해준다.
for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            flip(i, j)
            result += 1

        if a == b:
            break
    if a == b:
        break

if a != b:
    print(-1)
else:
    print(result)
