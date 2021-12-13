input = [4, 6, 2, 9, 1]

# 총 시간 복잡도  .최선의 경우 O(N), 아닌 경우 O(N**2)
# 거의 정렬이 된상태의 배열을 입력했을경우 더 좋은 결과를 얻을 수 있다.
def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i - j - 1] > array[i - j]:     # 예를 들어 i = 1, j = 0 일때, 0번째 어레이값과 1번째 어레이값을 비교
                                                    # 이전 어레이 값이 더 크다면 자리를 바꾼다.
                array[i - j - 1], array[i - j] = array[i - j], array[i - j -1]
            else:
                break       # 모두 다 비교 해보지 않고 앞에것만 비교해보고 아니면 바로 반복문을 끝낸다.
    return


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!