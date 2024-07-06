import numpy as np

def idx_of_the_nearest(data, value):
    idx = np.argmin(np.abs(np.array(data) - value))
    idx2 = np.argmin(np.abs(np.array(data)[::-1] - value))
    if idx == idx2:
        return [data[idx],data[idx]]
    else:
        global countType
        countType = True
        return [data[idx],data[idx2]]

N = int(input())
Ans = []
a_heights = list(map(int,input().split()))
b_heights = list(map(int,input().split()))
c_heights = list(map(int,input().split()))
d_heights = list(map(int,input().split()))
countType = False

for i in a_heights:
    b_head = idx_of_the_nearest(b_heights, i)
    c_head = idx_of_the_nearest(c_heights, i)
    d_head = idx_of_the_nearest(d_heights, i)
    if countType == False:
        Ans.append(max(i,b_head[0],c_head[0],d_head[0]) - min(i,b_head[0],c_head[0],d_head[0]))
    else:
        Ans_pre = []
        for b in b_head:
            for c in c_head:
                for d in d_head:
                    # 4 人の身長の最大値と最小値の差を求める
                    difference = max(i, b, c, d) - min(i, b, c, d)
                    # 差が更小な場合は更新する
                    min_difference = min(min_difference, difference)
        Ans.append(min(Ans_pre))
    countType = False

print(min(Ans))