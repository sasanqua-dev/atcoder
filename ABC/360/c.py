N = int(input())
box = list(map(int, input().split()))
weight = list(map(int, input().split()))

boxes = [[] for _ in range(N)]
for i in range(N):
    boxes[box[i] - 1].append(weight[i])

r = []

for b in boxes:
    if len(b) == 0:
        continue
    else:
        b.sort()
        b.remove(b[-1])
        r.append(sum(b))

print(sum(r))