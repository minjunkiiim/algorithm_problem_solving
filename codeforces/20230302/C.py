from queue import PriorityQueue
t = int(input())

for _ in range(t):
    n = int(input())
    deck = list(map(int, input().split(' ')))

    total_p = 0

    q = PriorityQueue()
    for card in deck:
        if card == 0:
            if not q.empty():
                total_p -= q.get()
        else:
            q.put(-card)

    print(total_p)