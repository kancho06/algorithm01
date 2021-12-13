input = [4, 6, 2, 9, 1]


# 총 시간 복잡도 O(N**2) -> 반복문 2번
def selection_sort(array):
    n = len(array)

    for i in range(n - 1):
        min_index = i
        for j in range(n - i):
            if array[i + j] < array[min_index]:     # 현재 돌고있는 index = i+j 가 min_index 보다 작다면
                min_index = i + j                   # 예를 들어 0 번째 i 에 4번째 j 라면  1이고
                                                    # min_index 가 4 이므로 min_index = 1 이 된다.
        array[i], array[min_index] = array[min_index], array[i]     # min_index 의 자리를 i 앞으로 바꿔준다.
    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!