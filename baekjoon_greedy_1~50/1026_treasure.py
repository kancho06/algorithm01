# 문제
# 옛날 옛적에 수학이 항상 큰 골칫거리였던 나라가 있었다.
# 이 나라의 국왕 김지민은 다음과 같은 문제를 내고 큰 상금을 걸었다.
#
# 길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자.
#
# S = A[0] × B[0] + ... + A[N-1] × B[N-1]
#
# S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열하면 안 된다.
#
# S의 최솟값을 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N이 주어진다.
# 둘째 줄에는 A에 있는 N개의 수가 순서대로 주어지고, 셋째 줄에는 B에 있는 수가 순서대로 주어진다.
# N은 50보다 작거나 같은 자연수이고, A와 B의 각 원소는 100보다 작거나 같은 음이 아닌 정수이다.
#
# 출력
# 첫째 줄에 S의 최솟값을 출력한다.

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sorted_a = sorted(a, reverse=True)
sorted_b = sorted(b)

s = 0
for i in range(n):
    s += sorted_a[i] * sorted_b[i]

print(s)

# 위처럼 내림차순 오름차순으로 정렬해서 간단히 제일 작은 수와 제일 큰 수를 곱해주면 되지만
# b 리스트는 재배열을 할 수 없다고 명시되어 있음으로 다른 방법을 사용


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sorted_a_list = sorted(a, reverse=False)    # a.sort()로 해도 됨. 그냥 해보고 싶었음

s = 0
for i in range(n):
    s += sorted_a_list[i] * max(b)
    b.pop(b.index(max(b)))

print(s)

# a는 재정렬을 하여 가장 작은 순서대로 sort 하고 b는 가장 큰순서대로 뽑아서 곱해준 후  pop를 이용하여 리스트에서 삭제
