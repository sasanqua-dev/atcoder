N = input()
A = list(map(int,input().split()))
B = list(map(int,input().split()))

a = [1 for i1,i2 in zip(A,B) if (i1 == i2)]

print(len(a))
print(len(set(A)&set(B)) - len(a))