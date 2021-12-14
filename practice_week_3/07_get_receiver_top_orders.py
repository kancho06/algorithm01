top_heights = [6, 9, 5, 7, 4]

# 문제
# 탑은 왼쪽으로 레이져를 쏘고 자기보다 높은 탑만이 수신할 수 있다.
# 수신한 탑의 인덱스 번호를 신호를 보낸 인덱스 자리에 출력하시오

# 총 시간 복잡도
#   O(N**2)
def get_receiver_top_orders(heights):
    answer = [0] * len(heights)
    while heights: # heights 가 빈 상태가 아닐때까지      O(N)
        height = heights.pop()
        for idx in range(len(heights) - 1, 0, -1):     # 마지막 6은 측정할 필요없으므로 heights - 1 해준다      O(N)
            if heights[idx] > height:       # 탑이 바뀌는 순간
                answer[len(heights)] = idx + 1      # answer[len(heights)] = 4번째 인덱스 = idx(3) + 1 = 즉 answer 의 4번째 인덱스는 4 가 된다.
                break
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!