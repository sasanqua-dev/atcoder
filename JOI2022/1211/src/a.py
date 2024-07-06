N =int(input())
A = list(map(int,input().split()))

max_value = max(A)
min_value = min(A)
for i in A:
    if abs(max_value-i) > abs(min_value-i):
        print(abs(max_value-i))
    else:
        print(abs(min_value-i))

