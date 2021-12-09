# 재귀함수는 무한루프에 빠질 수 있기때문에 빠져나올 지점을 잘 설정해주어야 한다.

def count_down(number):
    if number < 0:
        return
    print(number)
    count_down(number - 1) # count_down 함수를 number - 1 인자를 주고 다시 호출한다!


count_down(60)