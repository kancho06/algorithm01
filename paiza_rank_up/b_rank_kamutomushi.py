n = int(input())
r, g, b = map(int, input().split())
for i in range(n):
    t, c = map(input().split())
    if t == 'L':
        if c == 'R':
            r -= 1
        elif c == 'G':
            g -= 1
        elif c == 'B':
            b -= 1
        elif c == 'Y':
            r -= 1
            g -= 1
        elif c == 'C':
            g -= 1
            b -= 1
        elif c == 'M':
            r -= 1
            b -= 1
        else:
            r -= 1
            g -= 1
            b -= 1
    else:
        if c == 'R':
            r += 1
        elif c == 'G':
            g += 1
        elif c == 'B':
            b += 1
        elif c == 'Y':
            r += 1
            g += 1
        elif c == 'C':
            g += 1
            b += 1
        elif c == 'M':
            r += 1
            b += 1
        else:
            r += 1
            g += 1
            b += 1
    if r == g == b:
        print(r)
    elif n == i and r != g != b:
        print('no')



