# 문제
# 다음과 같은 문자열을 입력받았을 때, 어떤 알파벳이 가장 많이 포함되어 있는지 반환하시오.

input = "hello my name is sparta"


# 공간 복잡도
# 1. alphabet_array 의 길이 = 26
# 2. max_occurrence, max_alphabet, occurrence 변수 = 3
# 이 함수는 총 29 만큼의 공간이 사용됨
# 시간 복잡도
# 1. alphabet_array 의 길이 * 대입 연산 1번  (for 문)             // (20~21 번째 코드)
# 2. alphabet_array 의 길이 * string 의 길이 * (비교 연산 1번 + 대입 연산 1번)         // (22~24 번째 코드)
# 3. alphabet_array 의 길이 * (비교 연산 1번 + 대입 연산 2번)                    // (26~28 번째 코드)
# string 의 길이는 보통 N 이라고 표현
# 26 * (1 + 2 * N + 3) = 52N +104
# 상수는 제외하고 N 만큼의 시간이 필요하다고 생각
def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "g", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t", "u", "v", "w", "x", "y", "z"]

    max_occurrence = 0
    max_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:
        occurrence = 0
        for char in string:
            if char == alphabet:
                occurrence += 1

        if occurrence > max_occurrence:
            max_occurrence = occurrence
            max_alphabet = alphabet

    return max_alphabet


result = find_max_occurred_alphabet(input)
print(result)
