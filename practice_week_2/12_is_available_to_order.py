shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


# 방법 1
# 총 시간 복잡도 = O((M+N) * lonN)
# 복잡도가 복잡한 수식이되면 효율적이지 않다는 뜻
# def is_available_to_order(menus, orders):
#     shop_menus.sort()  # 정렬의 시간 복잡도는 배열의 길이를 N 이라고 할때
#     # O(N * logN) 이라고 한다.
#     for orders in orders:  # O(M * logN)
#         if not is_existing_target_number_binary(orders, menus):
#             return False
#     return True

# 방법 2
# set 이라는 집합 자료형은 중복되는 것을 다 없애주는 자료형
# ex. a = set[1,2,3,4,1,2,3]
# a = [1,2,3,4]
# 총 시간 복잡도 = O(N) + O(M) = O(N+M)
def is_available_to_order(menus, orders):
    menus_set = set(menus)  # O(N)
    for order in orders:  # O(M)
        if order not in menus_set:  # O(1)
            return False

    return True


def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2
    find_count = 0

    while current_min <= current_max:
        find_count += 1
        if array[current_guess] == target:
            print(find_count)
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2

    return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)
