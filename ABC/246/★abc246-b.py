import math
A = list(map(int,input().split()))
a = A[0]**2 + A[1]**2
a = math.sqrt(a)
print(A[0]/a,A[1]/a)