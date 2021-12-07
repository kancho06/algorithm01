# 문제
# 다음과 같이 숫자로 이루어진 배열이 있을때, 이 배열 내에서 가장 큰 수를 반환하시오.

input = [3, 5, 6, 1, 2, 4]


# 시간복잡도
# 1. 대입 연산 1번 + array 의 길이 * 비교연산 1번
# 1 + 2 * N = 2N + 1
def find_max_num(array):
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num

    return max_num


result = find_max_num(input)
print(result)
