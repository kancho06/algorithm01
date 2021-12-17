# 문제
# 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
# 이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
# 예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다.(11, 13, 17, 19)또, 14보다 크고, 28보다 작거나 같은 소수는
# 3개가 있다. (17, 19, 23)
# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 입력은 여러 개의 테스트케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.
# 입력의 마지막에는 0이 주어진다

# 출력
# 각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.

# 제한
# 1<= n <= 123,456

# 해법 1
# 에라토스테네스의 체를 이용한 방법
n = 123456 * 2 + 1  # n+1 < x < 2n 의 소수 범위 설정 (07 강의에서 배운 소수 )
sieve = [True] * n  # 소수 x의 개수를 카운트하기 모든 수를 true 로 생각
for i in range(2, int(n ** 0.5) + 1):  # 소수를 구하는 범위 2 ~ n+1 받은 범위에서
    if sieve[i]:
        for j in range(2 * i, n, i):
            sieve[j] = False


def prime_count(val):
    count = 0
    for i in range(val + 1, val * 2 + 1):  # 소수의 범위
        if sieve[i]:
            count += 1
    print(count)


while True:
    val = int(input())
    if val == 0:
        break
    prime_count(val)


