t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split(' ')))
    s = input()

    count = [0] * (ord('z') - ord('A') + 1)
    for c in s:
        count[ord(c) - ord('A')] += 1
    
    ret = 0

    for i in range(ord('Z') - ord('A') + 1):
        upper_c = count[i]
        lower_c = count[i + ord('a') - ord('A')]

        diff = abs(upper_c - lower_c)
        num_op = min(diff // 2, k)
        k -= num_op

        ret += min(upper_c, lower_c) + num_op

    print(ret) 
            