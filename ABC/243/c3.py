N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
D = list(str(input()))
X, Y = [list(i) for i in zip(*xy)]
a = [1 for i1,count1 in zip(Y,range(0,N)) for i2,count2 in zip(Y[(count1):],range(count1,N)) if (i1 == i2) and  ((((X[count1]) > (X[count2])) and (D[count1] == "L") and (D[count2] == "R")) or (((X[count1]) < (X[count2])) and (D[count1] == "R") and (D[count2] == "L"))) ]
if not a:
    print("No")
else:
    print("Yes")
