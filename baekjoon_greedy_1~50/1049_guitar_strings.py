# 문제
# Day Of Mourning의 기타리스트 강토가 사용하는 기타에서 N개의 줄이 끊어졌다.
# 따라서 새로운 줄을 사거나 교체해야 한다. 강토는 되도록이면 돈을 적게 쓰려고 한다.
# 6줄 패키지를 살 수도 있고, 1개 또는 그 이상의 줄을 낱개로 살 수도 있다.
#
# 끊어진 기타줄의 개수 N과 기타줄 브랜드 M개가 주어지고,
# 각각의 브랜드에서 파는 기타줄 6개가 들어있는 패키지의 가격,
# 낱개로 살 때의 가격이 주어질 때, 적어도 N개를 사기 위해 필요한 돈의 수를 최소로 하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N과 M이 주어진다.
# N은 100보다 작거나 같은 자연수이고, M은 50보다 작거나 같은 자연수이다.
# 둘째 줄부터 M개의 줄에는 각 브랜드의 패키지 가격과 낱개의 가격이 공백으로 구분하여 주어진다.
# 가격은 0보다 크거나 같고, 1,000보다 작거나 같은 정수이다.
#
# 출력
# 첫째 줄에 기타줄을 적어도 N개 사기 위해 필요한 돈의 최솟값을 출력한다.
import sys

n, m = map(int, sys.stdin.readline().split())
result = 0
p_price_list = []
o_price_list = []

for i in range(m):
    p, o = map(int, sys.stdin.readline().split())
    p_price_list.append(p)
    o_price_list.append(o)

p_min = min(p_price_list)
o_min = min(o_price_list)

if p_min < o_min * 6:  # 패키지의 가격이 낱개의 가격 * 6 보다 적을때
    if p_min < (n % 6) * o_min:  # 패키지의 가격이 끈어진 기타줄 패키지 산후 못고친 기타줄 * 낱개 보다 적을때
        print((n // 6) * p_min + p_min)  # 기타줄이 남게 되더라도 다 패키지로 구입
    else:
        print((n // 6) * p_min + (n % 6) * o_min)  # 패키지 + 낱개로 딱맞춰구입
elif p_min >= o_min * 6:  # 패키지의 가격이 낱개의 가격보다 같거나 높을때
    print(n * o_min)  # 전부 낱개로 구입
