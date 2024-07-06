N = int(input())
if N < 10:
    answer = [(i+1) for i in range(N)]
else:
    answer = [(i+1) % 9 for i in range(N-9)]
    answer.append(45)
print(answer)
print(sum(answer) % 998244353)
