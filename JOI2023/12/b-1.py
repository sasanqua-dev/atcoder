import sys
import numpy as np
from numba import jit
input = sys.stdin.readline

@jit
def main():
    N, M, Q = map(int, input().split())
    PA = np.array([list(map(int, input().split())) for _ in range(N)])
    TLR = np.array([list(map(int, input().split())) for _ in range(Q)])

    price_by_day = np.zeros((M, len(PA)))

    for m in range(M):
        for i, pa in enumerate(PA):
            if pa[1] == m + 1:
                price_by_day[m, i] = pa[0] // 2
            else:
                price_by_day[m, i] = pa[0]

    for tlr in TLR:
        print(np.sum(price_by_day[tlr[0]-1, tlr[1]-1:tlr[2]]))

if __name__ == '__main__':
    main()