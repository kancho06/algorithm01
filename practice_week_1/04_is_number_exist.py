# 문제
# 다음과 같은 숫자로 이루어진 배열이 있을 때, 이 배열 내에 특정 숫자가 존재한다면 True,
# 존재하지 않다면 False 를 반환하시오.

input = [3, 5, 6, 1, 2, 4]


# 시간 복잡도
# 1. array 의 길이 (for 문)
# 2. 비교 연산 1번
# N * 1 = N 만큼의 시간 복잡도
# 3 이 아닌 4 가 입력값이 였다면 성능이 동일하지 않다 (4가 배열상 맨 뒤에 있음으로)
# 입력값이 좋을때 1 , 안 좋을 때 N
# 빅 오메가 Ω(1), 빅 오 O(N)
def is_number_exist(number, array):
    for element in array:         # 1
        if number == element:         # 2
            return True             # N * 1 = N 만큼의 시간 복잡도

    return False


result = is_number_exist(3, input)
print(result)
