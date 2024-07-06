N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
D = list(str(input()))
X, Y = [list(i) for i in zip(*xy)]
count1 = -1

for i1 in Y:
    count1 += 1
    count2 = count1
    for i2 in Y[(count1):]:
        count2 += 1
        if i1 == i2:
            if (((X[count1]) > (X[count2])) and (D[count1] == "L") and (D[count2] == "R")) or (((X[count1]) < (X[count2])) and (D[count1] == "R") and (D[count2] == "L")):
                print("Yes")
                exit()
  
print("No")
