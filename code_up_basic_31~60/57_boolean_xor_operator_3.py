# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 모두 False 일 때에만 True 를 출력하는 프로그램을 작성해보자.
#
# 경우의수
# c = true  d = true    결과 = false
# c = true  d = false   결과 = false
# c = false d = false   결과 = true
# 둘다 false 일때만 true 반환


a, b = map(int, input().split())
c, d = bool(a), bool(b)

print(not (c or d))