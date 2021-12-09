input = "abcba"


def is_palindrome(string):
    n = len(string)
    for i in range(n):
        if string[i] != string[n - 1 - i]:  # 첫번째가 0 맨뒤가 n - 1이므로
            return False

    return True


print(is_palindrome(input))