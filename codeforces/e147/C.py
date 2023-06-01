t = int(input())

for _ in range(t):
    s = input()

    letters = set(s)

    min_cost = len(s)
    for letter in letters:
        max_interval = 0
        curr_interval = 0
        for c in s:
            if c == letter:
                max_interval= max(max_interval, curr_interval)
                curr_interval = 0

            else:
                curr_interval += 1

        max_interval = max(max_interval, curr_interval)

        cost = 0
        while max_interval > 0:
            max_interval = max_interval // 2
            cost += 1

        min_cost = min(min_cost, cost)

    print(min_cost)
