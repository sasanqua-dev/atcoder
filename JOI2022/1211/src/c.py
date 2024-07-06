H,W = map(int,input().splite())
# 各マスの状態を取得する
colors = [[int(input()) for _ in range(W)] for _ in range(H)]

# 塗りつぶしを行う
x, y, c = map(int, input().split())
colors[x-1][y-1] = c

# マス (x, y) の領域内に含まれるマスの数を求める
count = 0
visited = [[False for _ in range(W)] for _ in range(H)]

# 幅優先探索を行う
queue = deque([(x-1, y-1)])
while queue:
    x, y = queue.popleft()
    if visited[x][y]:
        continue
    visited[x][y] = True
    count += 1

    # 上下左右のマスを探索する
    if x > 0 and colors[x-1][y] == c and not visited[x-1][y]:
        queue.append((x-1, y))
    if x < H-1 and colors[x+1][y] == c and not visited[x+1][y]:
        queue.append((x+1, y))
    if y > 0 and colors[x][y-1] == c and not visited[x][y-1]:
        queue.append((x, y-1))
    if y < W-1 and colors[x][y+1] == c and not visited[x][y+1]:
        queue.append((x, y+1))

# 結果を出力する
print(count)
