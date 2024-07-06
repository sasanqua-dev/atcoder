import numpy as np

def idx_of_the_nearest(data, value):
    data = list(data)
    data = sorted(data)
    idx = np.argmin(np.abs(np.array(data) - value))
    if len(data) < 2 or idx == (len(data)-1):
        return [data[idx],data[idx]]
    else:
        return [data[idx],data[idx+1]]

N = int(input())
Ans = []
a_heights = set(map(int,input().split()))
b_heights = set(map(int,input().split()))
c_heights = set(map(int,input().split()))
d_heights = set(map(int,input().split()))

for i in a_heights:
    b_head = idx_of_the_nearest(b_heights, i)
    c_head = idx_of_the_nearest(c_heights, i)
    d_head = idx_of_the_nearest(d_heights, i)
    for b in b_head:
        for c in c_head:
            for d in d_head:
                Ans.append(max(i, b, c, d) - min(i, b, c, d))
print(min(Ans))