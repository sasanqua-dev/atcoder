import re
import numpy as np
h,w =map(int,input().split())
A_dict = np.zeros((h,w))
for i1 in range(h):
    a_input = list(map(int,input().split()))
    for i in range(w):
        A_dict[i1][i] = a_input[i]

A_dict = (A_dict.T)

result = [[str(round(int(a))) for a in A_dict[i]] for i in range(w)]
for i in range(w):
    print(" ".join(result[i]))


