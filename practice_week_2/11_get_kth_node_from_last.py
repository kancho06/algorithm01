class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    # 방법 1
    # 1. LinkedList 길이 전부 알아내기 O(N)
    # 2. 그 길이에서 k 만큼 뺀 길이만큼 이동 O(N-k)
    # def get_kth_node_from_last(self, k):
    #     length = 1  # 시작 노드의 길이를 세기 위해 1부터 시작합니다
    #     cur = self.head
    #
    #     while cur.next is not None:
    #         cur = cur.next
    #         length += 1
    #     end_length = length - k
    #     cur = self.head
    #     for i in range(end_length):
    #         cur = cur.next
    #     return cur

    # 방법 2
    # 1. 노드를 두개 잡는다.
    # 2. 한 노드를 다른 노드보다 k 만큼 떨어지게 한다.
    # 3. 그리고 계속 한 칸씩 같이 이동한다.
    # 4. 만약 더 빠른 노드가 끝에 도달했다면
    # 느린 노드는 끝에서 k 만큼 떨어진 노드가 되므로
    # 바로 반환하자. O(N) O(N-k)
    def get_kth_node_from_last(self, k):
        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next

        while fast is not None:
            fast = fast.next
            slow = slow.next

        return slow


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!