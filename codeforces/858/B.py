t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(' ')))

    zeros = 0
    ones = 0
    for a_ in a:
        if a_ == 0:
            zeros += 1
        elif a_ == 1:
            ones += 1

    if zeros <= (n + 1) // 2:
        print(0)
    elif ones > 0 and zeros + ones == n:
        print(2)
    else:
        print(1)
