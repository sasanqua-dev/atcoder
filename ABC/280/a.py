H , W = map(int,input().split())
block = []
a_block = []
for i in range(H):
    block.append(list(input()))

for i in block:
    for j in i:
        a_block.append(j)
answer = a_block.count('#')
print(answer)