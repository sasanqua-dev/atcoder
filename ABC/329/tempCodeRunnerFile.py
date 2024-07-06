from collections import Counter

t = int(input())
A = list(map(int, input().split()))
counter = Counter()
mm = None

for a in A:
    counter[a] += 1
    if mm is None or counter[a] > counter[mm[0]]:
        mm = [a]
    elif counter[a] == counter[mm[0]]:
        mm.append(a)

    mm.sort()
    print(mm[0])
