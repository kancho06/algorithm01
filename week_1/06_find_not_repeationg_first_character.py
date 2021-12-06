# 문제
# 다음과 같이 영어로 되어 있는 문자열이 있을 때, 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오. 만약 그런 문자가 없다면 _를 반환하시오.

input = "abadabac"


# 시간 복잡도
# 1. 대입 연산 1번
# 2. array 의 길이 N * (비교 연산 1번 + 대입 연산 1번)
# 3. array 의 길이 N * (대입 연산 1번 + 비교 연산 1번)
# 4. array 의 길이 N * 비교 연산 1번
# N * 2 + N * 2 + N * 1 = 5N
# 상수 제외하고 O(N), Ω(1)
def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1
    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord("a")))

    # c 가 반환됨으로 우리는 input 에 반복되지 않는 첫번째 문자인 d를 반환시켜 주기위해 for 문을 한번더 돌린다.
    for char in string:
        if char in not_repeating_character_array:
            return char


result = find_not_repeating_character(input)
print(result)
