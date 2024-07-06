import sys
import numpy as np

def main():
    N, M, Q = map(int, input().split())
    PA = np.array([list(map(int, input().split())) for _ in range(N)])
    TLR = np.array([list(map(int, input().split())) for _ in range(Q)])

    # 商品ごとの日ごとの価格を計算
    price_by_day = np.zeros((M, N), dtype=int)
    for m in range(1, M + 1):
        mask = PA[:, 1] == m
        price_by_day[m - 1] = PA[:, 0] // 2 * mask
        price_by_day[m - 1] += np.sum(price_by_day[:, ~mask], axis=1)

    # クエリごとに回答
    for tlr in TLR:
        result = np.sum(price_by_day[tlr[0] - 1, tlr[1] - 1:tlr[2]])
        print(result)

if __name__ == "__main__":
    main()
