N = int(input())
# クラス内の生徒の身長を取得する
a_heights = list(map(int,input().split()))
b_heights = list(map(int,input().split()))
c_heights = list(map(int,input().split()))
d_heights = list(map(int,input().split()))

# 代表を選ぶための最小の差
min_difference = float("inf")
# 結果を出力する
print(min([(max(a, b, c, d) - min(a, b, c, d)) for d in d_heights for c in c_heights for b in b_heights for a in a_heights]))