# n = ord(input())  #입력받은 문자를 10진수 유니코드 값으로 변환한 후, n에 저장한다.
#
# ord( ) 는 어떤 문자의 순서 위치(ordinal position) 값을 의미한다.
# 실제로 각각의 문자들에는 연속된 정수 값이 순서에 따라 부여 되어 있다. A:65, B:66, C:67 ....
# ord(c) : 문자 c 를 10진수로 변환한 값
#
# 컴퓨터로 저장되고 처리되는 모든 데이터들은 2진수 형태로 정수화 되어야 하는데,
# 컴퓨터에 문자를 저장하는 방법으로 아스키코드(ASCII Code)나 유니코드(Unicode)가 자주 사용된다.
#
# 예를 들어, 영문 대문자 'A'는 10진수 값 65 로 표현하고,
# 2진수(binary digit) 값 1000001 로 바꾸어 컴퓨터 내부에 저장한다.
#
# 유니코드(unicode)는 세계 여러 나라의 문자를 공통된 코드 값으로 저장할 때 사용하는 표준 코드이다.


n = ord(input())
print(n)