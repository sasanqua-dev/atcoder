import sys
from operator import itemgetter
from collections import deque
input = sys.stdin.readline

import pypyjit
pypyjit.set_param("max_unroll_recursion=-1")

def main():
    N,M,Q = map(int,input().split())
    PA = [list(map(int,input().split())) for _ in range(N)]
    TLR = [list(map(int,input().split())) for _ in range(Q)]

    price_by_day = [[int(pa[0]/2) if pa[1] == m+1 else pa[0] for pa in PA] for m in range(M)]

    for tlr in TLR:
        print(sum(price_by_day[tlr[0]-1][tlr[1]-1:tlr[2]]))

if __name__ == '__main__':
    main()