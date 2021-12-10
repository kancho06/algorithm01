numbers = [2, 3, 1]
target_number = 0

# N 의 길이의 배열에서 더하거나 뺀 모든 경우의 수는
# N - 1 의 길이의 배열에서 마지막 원소를 더하거나 뺀 경우의 수를
# 추가하면 된다.
# ex. [2, 3, 1]
# 1. +2 +3  (+1)  = +2 +3 +1
#           (-1)  = +2 +3 -1
# 2. +2 -3  (+1)  = +2 -3 +1
#           (-1)  = +2 -3 -1
# 3. -2 +3  (+1)  = -2 +3 +1
#           (-1)  = -2 +3 -1
# 4. -2 -3  (+1)  = -2 -3 +1
#           (-1)  = -2 -3 -1
result = []
result_count = 0


# all_ways = result = []
# current_index = 0
# current_sum = 0
# array =[2, 3, 1]
# 외부 문자열이나 숫자열이 함수로 들어갓다가 다시나오면 초기화되기 때문에 global 을 써준다
def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum):
    if current_index == len(numbers):
        if current_sum == target:
            global result_count
            result_count += 1
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(
        array, target, current_index + 1, current_sum + numbers[current_index]
    )  # array, 1, 0 + 2, all_ways
    get_count_of_ways_to_target_by_doing_plus_or_minus(
        array, target, current_index + 1, current_sum - numbers[current_index]
    )  # array, 1, 0 - 2, all_ways


get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0)  # 5를 반환해야 합니다!
print(result_count)
