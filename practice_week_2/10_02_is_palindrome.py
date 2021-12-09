input = "abcba"


def is_palindrome(string):
    if len(string) <= 1:
        return True

    if string[0] != string[-1]:
        return False

    return is_palindrome(string[1:-1])

# 에러코드
# def is_palindrome2(string):
#     print(string)
#     if len(string) == 1:
#         return True
#     if string[0] == string[-1]:
#         is_palindrome2(string[1:-1])
#     else:
#         return False


print(is_palindrome(input))
