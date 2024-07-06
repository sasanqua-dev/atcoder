N = int(input())
S = [list(input()) for _ in range(N)]

row_counts = [0] * N
col_counts = [0] * N
for i in range(N):
    for j in range(N):
        if S[i][j] == "o":
            row_counts[i] += 1
            col_counts[j] += 1

print(sum([(row_counts[i]-1)*(col_counts[j]-1) for i in range(N) for j in range(N) if S[i][j] == "o"]))