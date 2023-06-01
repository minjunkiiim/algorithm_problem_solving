A, X, M = list(map(int, input().split(' ')))

mod_list = [1] * M

for i in range(1, M):
    k = mod_list[i - 1]
    k = (k * A + 1) % M
    mod_list[i] = k
    

print(mod_list)