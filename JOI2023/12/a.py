import sys
from operator import itemgetter
from collections import deque
import numpy as np
input = sys.stdin.readline

N = int(input())
A = [int(a) for a in input().split()]

sorted(set(A))
r = "No"

for ai,a in enumerate(a):
    if a+3 in A:
        if a+6 in A:
            r = "Yes"
            break
    
print(r)