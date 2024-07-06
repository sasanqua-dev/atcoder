import sys
import numpy as np

input = sys.stdin.readline
N, M, Q = map(int, input().split())
PA = np.array([list(map(int, input().split())) for _ in range(N)])
TLR = np.array([list(map(int, input().split())) for _ in range(Q)])

price_by_day = PA[:, 0] // 2 * (PA[:, 1] == np.arange(1, M + 1))

for tlr in TLR:
    print(np.sum(price_by_day[tlr[0] - 1, tlr[1] - 1:tlr[2]]))
