from collections import defaultdict

N, T = map(int, input().split())
S = input()
X = list(map(int, input().split()))

left_indices = defaultdict(list)
right_indices = defaultdict(list)

for i in range(N):
    if S[i] == '0':
        left_indices[X[i] - T * 2].append(i)
    else:
        right_indices[X[i] + T * 2].append(i)

result = 0
for i in range(N):
    if S[i] == '0':
        for j in right_indices.keys():
            if X[i] < j:
                result += len(right_indices[j])
    else:
        for j in left_indices.keys():
            if X[i] > j:
                result += len(left_indices[j])

print(result)