# 문제
# 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.

input = 20


def find_prime_list_under_number(number):

    prime_list = []
    # 이 식이 비효율 적인 이유
    # 예를들어,  n = 19
    # i = 2, 3, 4, 5, 6, 7, 8 .... 18
    # 2(로 나누면) -> X / 3 -> X / 6 -> X
    # 2, 3으로도 나누어지지않았는데 2 * 3 으로 이루어진 6으로는 당연히 나누어지지 않는다.
    # 그래서 i 의 범위를 소수로만 제한시킨다.
    # i = 2, 3, 5, 7, ....
    # for n in range(2, number + 1):  # n 의 범위 2부터 number 까지
    #     for i in range(2, n): # i 의 번위 2부터 n - 1 까지
    #         if n % i == 0:
    #             break
    #     else:
    #         prime_list.append(n)
    # return prime_list

    # prime_list 가 빈배열로 시작해서 n 이 소수가 들어갈때 하나씩 배열에 추가된다.
    # 하지만 좀 더 효율적인 방법이 존재한다.
    # 소수의 특징을 다시 한번 생각해보자.
    # 주어진 자연수 N이 소수이기 위한 필요 충분 조건은
    # N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다
    # 수가 수를 나누면 몫이 발생하는데, 몫과 나누는 수 둘 중 하나는
    # 반드시 N의 제곱근의 이하
    # for n in range(2, number + 1):
    #     for i in prime_list:
    #         if n % i == 0:
    #             break
    #     else:
    #         prime_list.append(n)
    #
    # return prime_list

    # 마지막 리팩토링
    # i 의 대조 회수가 적어지기 때문에 효율이 더 좋아졌다.
    for n in range(2, number + 1):
        for i in prime_list:
            if n % i == 0 and i * i <= n:
                break
        else:
            prime_list.append(n)
    return prime_list


result = find_prime_list_under_number(input)
print(result)