# 10진수 형태로 입력받고
# %X로 출력하면 16진수(hexadecimal)대문자로 출력된다.
#
# 16진법은 영문 소문자를 사용하는 경우에 한 자리에 16개(0 1 2 3 4 5 6 7 8 9 A B C D E F)의 문자를 사용한다.
# 16진수 A는 10진수의 10, B는 11, C는 12 ... 와 같다.

a = input()
n = int(a)
print('%X' % n)