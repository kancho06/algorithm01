
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
#                  factorial(1) 에서 if 문 리턴 1
# 5 * 4 * 3 * 2 * 1
def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n -1)


print(factorial(5))