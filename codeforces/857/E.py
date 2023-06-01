t = int(input())

for _ in range(t):
    n = int(input())
    albums = []
    
    for i in range(n):
        albums.append([])
        k = int(input())
        a = list(map(int, input().split(' ')))

        m = -1
        for track in a:
            if track > m:
                albums[i].append(track)
                m = track

    print(albums)
