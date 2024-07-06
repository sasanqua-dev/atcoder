import random
N = random.randint(1, 75000)
A = [random.randint(1, 500) for i in range(N)]
B = [random.randint(1, 500) for i in range(N)]
C = [random.randint(1, 500) for i in range(N)]
D = [random.randint(1, 500) for i in range(N)]
print(N)
print(*A)
print(*B)
print(*B)
print(*B)