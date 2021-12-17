# 문제
# 극장의 좌석은 한 줄로 되어 있으며 왼쪽부터 차례대로 1번부터 N번까지 번호가 매겨져 있다.
# 공연을 보러 온 사람들은 자기의 입장권에 표시되어 있는 좌석에 앉아야 한다.
# 예를 들어서, 입장권에 5번이 쓰여 있으면 5번 좌석에 앉아야 한다.
# 단, 자기의 바로 왼쪽 좌석 또는 바로 오른쪽 좌석으로는 자리를 옮길 수 있다.
# 예를 들어서, 7번 입장권을 가진 사람은 7번 좌석은 물론이고,
# 6번 좌석이나 8번 좌석에도 앉을 수 있다.
# 그러나 5번 좌석이나 9번 좌석에는 앉을 수 없다.
# 그런데 이 극장에는 “VIP 회원”들이 있다.
# 이 사람들은 반드시 자기 좌석에만 앉아야 하며 옆 좌석으로 자리를 옮길 수 없다.
# 예를 들어서,
# 그림과 같이 좌석이 9개이고,
# 4번 좌석과 7번 좌석이 VIP석인 경우에 <123456789>는 물론 가능한 배치이다.
# 또한 <213465789> 와 <132465798> 도 가능한 배치이다.
# 그러나 <312456789> 와 <123546789> 는 허용되지 않는 배치 방법이다.
# 오늘 공연은 입장권이 매진되어 1번 좌석부터 N번 좌석까지 모든 좌석이 다 팔렸다.
# 총 좌석의 개수와 VIP 회원들의 좌석 번호들이 주어졌을 때,
# 사람들이 좌석에 앉는 서로 다른 방법의 가짓수를 반환하시오.

seat_count = 9
vip_seat_array = [4, 7]

# [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5] 의 경우의 수는 2, 3, 5, 8 이 나온다.
# 피보나치 수열을 사용하도록 하자
# 원래는
# F(1) = 1
# F(2) = 2
# 이지만
# 좌석(2) = 2
# 좌석(3) = 3
# 의 모습을 보이고있다.
# 4와 7 은 고성석이므로,
# 1, 2, 3 F(3) = 3
# 5, 6    F(2) = 2
# 8, 9    F(2) = 2
# 곱의 법칙에 의해서
# 3 * 2 * 2 = 12 가지 경우의 수가 나온다.

memo = {
    1: 1,
    2: 2
}

def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_ways = 1
    current_index = 0
    for fixed_seat in fixed_seat_array:
        fixed_seat_index = fixed_seat - 1       # vip 좌석 번호를 인덱스 번호로 바꾼다.
        count_of_ways = fibo_dynamic_programming(fixed_seat_index - current_index, memo)  # vip 좌석 idx(3) - 현재 index (0) = 4 이므로 1~4 사이에 1, 2, 3 의 경우의 수를 구할 수 있다.
        all_ways *= count_of_ways       # 곱연산으로 경우의 수에다가 곱해준다. 1 * 3
        current_index = fixed_seat_index + 1        # 4 다음의 인덱스를 봐야하니 + 1 을 해준다.

    count_of_ways = fibo_dynamic_programming(total_count - current_index, memo)
    all_ways *= count_of_ways
    return all_ways


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))