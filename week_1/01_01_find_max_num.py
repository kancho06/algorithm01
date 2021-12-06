input = [3, 5, 6, 1, 2, 4]


# 시간복잡도
# 1. array 의 길이 * array 의 길이 + 비교 연산 1번
# N * N + 1
def find_max_num(array):
    for num in array:
        for compare_num in array:
            if num < compare_num:
                break
        else:
            return num


result = find_max_num(input)
print(result)
