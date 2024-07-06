import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

N, T = map(int, input().split())
S = input()
Slist = [int(i) for i in list(S)]
X = list(map(int, input().split()))

result = 0
for i in range(int(N)):
    position = X[i]
    direction = Slist[i]
    for j in range(i+1, N):
        if Slist[j] == direction:
            continue
        if Slist[j] != direction and position < X[j] and direction == 1 and X[j] - position <= T * 2:
            result += 1
        elif Slist[j] != direction and position > X[j] and direction == 0 and position - X[j] <= T * 2:
            result += 1
print(result)