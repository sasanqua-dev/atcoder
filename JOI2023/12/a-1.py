import sys
import numpy as np

N = int(input())
A = np.array(list(map(int, input().split())))

unique_A = np.unique(A)
unique_A_set = set(unique_A)

r = "No"

for a in unique_A:
    if a + 3 in unique_A_set and a + 6 in unique_A_set:
        r = "Yes"
        break

print(r)
