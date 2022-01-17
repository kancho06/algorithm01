# 월이 입력될 때 계절 이름이 출력되도록 해보자.
#
# 월 : 계절 이름
# 12, 1, 2 : winter
#   3, 4, 5 : spring
#   6, 7, 8 : summer
#   9, 10, 11 : fall

m = int(input())

if m//3 == 1:
    print('spring')
elif m//3 == 2:
    print('summer')
elif m//3 == 3:
    print('fall')
else:
    print('winter')