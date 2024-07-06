N = str(input())
A = list(map(int, input().split()))

idx = A.index(-1)
answer = [idx+1]
for a, index in enumerate(A):
    if a == -1:
        continue
    if (index+1) in answer:
        idx = answer.index(index+1)
        answer.insert(idx, a)
    elif a in answer:
        idx = answer.index(a)
        answer.insert(idx+1, index+1)
    else:
        answer.append(index+1)
        answer.append(a)

print(answer)
