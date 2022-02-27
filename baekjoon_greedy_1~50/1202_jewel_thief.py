# 문제
# 세계적인 도둑 상덕이는 보석점을 털기로 결심했다.
#
# 상덕이가 털 보석점에는 보석이 총 N개 있다. 각 보석은 무게 Mi와 가격 Vi를 가지고 있다.
# 상덕이는 가방을 K개 가지고 있고, 각 가방에 담을 수 있는 최대 무게는 Ci이다.
# 가방에는 최대 한 개의 보석만 넣을 수 있다.
#
# 상덕이가 훔칠 수 있는 보석의 최대 가격을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N, K ≤ 300,000)
#
# 다음 N개 줄에는 각 보석의 정보 Mi와 Vi가 주어진다. (0 ≤ Mi, Vi ≤ 1,000,000)
#
# 다음 K개 줄에는 가방에 담을 수 있는 최대 무게 Ci가 주어진다. (1 ≤ Ci ≤ 100,000,000)
#
# 모든 숫자는 양의 정수이다.
#
# 출력
# 첫째 줄에 상덕이가 훔칠 수 있는 보석 가격의 합의 최댓값을 출력한다.
import heapq
import sys

n, k = map(int, input().split())
j_list = []
for i in range(n):
    heapq.heappush(j_list, list(map(int, sys.stdin.readline().split())))

bags = []

for _ in range(k):
    bags.append(int(sys.stdin.readline()))

j_list.sort()
bags.sort()

result = 0
j_bags = []

for bag in bags:
    while j_list and bag >= j_list[0][0]:       # 보석무게가 가방무게보다 작거나 같은 보석을 넣는다
        heapq.heappush(j_bags, -j_list[0][1])       # max heap 값을 - 로 하면 맥스힙
        heapq.heappop(j_list)       # 들어간 보석은 리스트에서 제거
    if j_bags:  # 가방에 옮겼으면 삭제시키고 result 에 보석가치 더하기
        result += heapq.heappop(j_bags)
    elif not j_list:    # 주얼리 리스트가 없으면 반복문 종료
        break

print(-result)