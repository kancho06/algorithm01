# 문제
# 다음과 같은 문자열을 입력받았을 때, 어떤 알파벳이 가장 많이 포함되어 있는지 반환하시오.

input = "hello my name is sparta"


# 공간 복잡도
# alphabet_array 의 길이 = 26
# arr_index, max_occurrence, max_alphabet_index, alphabet_occurrence 변수 = 4
# 이 함수는 총 30 만큼의 공간이 사용됨
# 공간을 더 적게 쓴 첫 번째 방법이 더 효율적일까?
# 29와 30 모두 상수라 큰 상관이 없다. 대부분의 문제에서는 알고리즘의 성능이 공간에 의해서 결정되지 않는다
# 따라서 공간 복잡도보다는 시간 복잡도를 더 신경 써야 한다.
# 시간 복잡도
# 1. string 의 길이 * (비교 연산 1번 + 대입 연산 2번)  (for 문)
# 2. 대입 연산 2번
# 3. alphabet_array 의 길이 * (비교 연산 1번 + 대입 연산 3번)  (for 문)
# string 의 길이는 보통 N 이라고 표현
# N * (1 + 2) + 2 + 26 * (1 + 3) = 3N + 106
# 상수는 제외하고 N 만큼의 시간이 필요하다고 생각
def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence > max_occurrence:
            max_alphabet_index = index
            max_occurrence = alphabet_occurrence

    return chr(max_alphabet_index + ord("a"))


result = find_max_occurred_alphabet(input)
print(result)
