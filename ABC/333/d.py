import numpy as np
N = int(input())
UV = sorted([list(map(int,input().split())) for _ in range(N-1) ], key=lambda x: x[0])
tree = []
for uv in UV:
    if uv[0] == 1:
        tree.append([uv[1]])
    else:
        for index,tr in enumerate(tree):
            if uv[0] in tr:
                tr.append(uv[1])
            elif uv[1] in tr:
                tr.append(uv[0])

least = sorted([len(tr) for _,tr in enumerate(tree)])
least[-1] = 1
print(sum(least))