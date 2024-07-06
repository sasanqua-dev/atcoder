N = int(input())
A = list(map(int, input().split()))
P = list(map(int, input().split()))
len_P = len(P)
add = []
init = A[0]
for i in range(2):
    for p, number in zip(P, range(len(P))):
        A[p-1] = A[p-1] + A[number+1]
        if (p-1) == 0:
            add.append(A[number+1])

if sum(add) < 0:
    print("-")
elif sum(add) == 0:
    if init > 0:
        print("+")
    elif init == 0:
        print("0")
    else:
        print("-")
else:
    print("+")
