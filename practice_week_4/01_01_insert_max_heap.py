
# 완전 이진트리의 최대 높이는 O(log(N))
# 그러면, 반복하는 최대 횟수도 O(log(N)) 이다.
# 즉, 맥스 힙의 원소 추가는 O(log(N)) 만큼의 시간 복잡도를 가진다고 할 수 있다.
class MaxHeap:
    def __init__(self):
        self.items = [None]  # 완전 이진 트리를 구현하기위해 0번째 인덱스를 None 으로 해준다.

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1  # None 은 제외 시킨다

        while cur_index > 1:
            parent_index = cur_index // 2  # 부모 노드 수식
            if self.items[cur_index] > self.items[parent_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break
        return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!
