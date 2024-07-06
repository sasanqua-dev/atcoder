import random
N = random.randint(3, 10)
A = [random.randint(1, 500) for i in range(N)]
B = [random.randint(1, 500) for i in range(N)]
C = [random.randint(1, 500) for i in range(N)]
D = [random.randint(1, 500) for i in range(N)]
print(N)
print(*A)
print(*B)
print(*C)
print(*D)