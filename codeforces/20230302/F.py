n = int(input())

counts = []
lenlist = []
zcounts = []
for i in range(n):
    clist = [0] * 26
    s = input()
    lenlist.append(len(s))
    for c in s:
        clist[ord(c) - ord('a')] += 1
    counts.append(clist)
    zc = 0
    for count in counts[i]:
        if count == 0:
            zc += 1
    zcounts.append(zc)

ret = 0

for i in range(n):
    clist1 = counts[i]

    for j in range(i + 1, n):
        if lenlist[i] ^ lenlist[j] == 0:
            continue
        if zcounts[i] + zcounts[j] > 27:
            continue

        clist2 = counts[j]
        zcount = 0
        for k in range(26):
            count = clist1[k] + clist2[k]
            if count == 0:
                zcount += 1
                if zcount > 1:
                    break
            elif count % 2 == 0:
                zcount = 2
                break

        if zcount == 1:
            ret += 1

print(ret)
