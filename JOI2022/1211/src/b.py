N = int(input())
# クラス内の生徒の身長を取得する
a_heights = list(map(int,input().split()))
b_heights = list(map(int,input().split()))
c_heights = list(map(int,input().split()))
d_heights = list(map(int,input().split()))

# 代表を選ぶための最小の差
min_difference = float("inf")

# 各クラスから代表を選ぶ
for a in a_heights:
    for b in b_heights:
        for c in c_heights:
            for d in d_heights:
                # 4 人の身長の最大値と最小値の差を求める
                difference = max(a, b, c, d) - min(a, b, c, d)
                # 差が更小な場合は更新する
                min_difference = min(min_difference, difference)

# 結果を出力する
print(min_difference)