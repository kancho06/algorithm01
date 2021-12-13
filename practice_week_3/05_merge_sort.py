array = [5, 3, 2, 1, 6, 8, 7, 4]

# 총 시간 복잡도
# 1. array 의 길이 N
# 2. N/2 를 2개 비교하면서 합친다. = N
# 3. N/4 를 2개씩 비교하면서 합친다. = N
# 4. N/8 을 2개씩 비교하면서 합친다. = N
# 모든 단계에서 N만큼의 시간 복잡도가 걸리므로
# log2N * O(N) -> O(NlogN) 만큼의 시간 복잡도
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])
    print(array)
    print('left_array', left_array)
    print('right_array',right_array)
    return merge(left_array, right_array)

# 시간 복잡도
# O(N) -> array1 + array2 = array 즉 반으로 나눈 배열들이 다시 합쳐져서 N이 되므로 N만큼 시간이 걸린다.
def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1

    return result


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!