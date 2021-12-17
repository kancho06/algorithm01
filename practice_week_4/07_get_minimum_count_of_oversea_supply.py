import heapq

# 문제
# 라면 공장에서는 하루에 밀가루를 1톤씩 사용합니다. 원래 밀가루를 공급받던 공장의 고장으로 앞으로
# k일 이후에야 밀가루를 공급받을 수 있기 때문에 해외 공장에서 밀가루를 수입해야 합니다.
# 해외 공장에서는 향후 밀가루를 공급할 수 있는 날짜와 수량을 알려주었고, 라면 공장에서는 운송비를 줄
# 이기 위해 최소한의 횟수로 밀가루를 공급받고 싶습니다.
# 현재 공장에 남아있는 밀가루 수량 stock, 밀가루 공급 일정(dates)과 해당 시점에 공급 가능한 밀가루 수
# 량(supplies), 원래 공장으로부터 공급받을 수 있는 시점 k가 주어질 때, 밀가루가 떨어지지 않고 공장을
# 운영하기 위해서 최소한 몇 번 해외 공장으로부터 밀가루를 공급받아야 하는지를 반환하시오.
# dates[i]에는 i번째 공급 가능일이 들어있으며, supplies[i]에는 dates[i] 날짜에 공급 가능한 밀가루 수
# 량이 들어 있습니다.


ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


# stock = 현재 재고량
# dates = 공급 해주는 날짜
# supplies = 공급량
# k = 원래 공장으로부터 공급받을 수 있는 시점, k 이후 부터는 공급받지 않아도 된다.
# k 이전에 공급량을 맞출 수 있는 최소한의 횟수
# 현재 재고가 바닥나는 시점 이전까지 받을 수 있는 밀가루 중 제일 많은 양의 밀가루를 받아야한다.
# 즉 stock <= k 가 되야한다.
# 1. 현재 재고의 상태에 따라 최솟값을 받아야 한다. -> 동적으로 변경되는 상황
# 2. 제일 많은 값, 제일 큰 값을 뽑아내야한다.
# heap 사용

def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0
    last_added_date_index = 0
    max_heap = []

    while stock <= k:
        while last_added_date_index < len(dates) and dates[last_added_date_index] <= stock:
            heapq.heappush(max_heap,
                           -supplies[last_added_date_index])  # [-20] 담겨있는 상태   % 힙큐는 min heap 밖에 지원하지 않아서 -를 나중에 벗겨준다.
            last_added_date_index += 1
        answer += 1
        heappop = heapq.heappop(max_heap)  # 최솟값 뽑기 [-20] 뽑아짐
        stock += -heappop  # +로 값 변경해서 더해줌
    return answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
