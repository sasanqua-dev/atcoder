N = int(input())
A = list(map(int,input().split()))
I = 0
Pizz = [360]
for i in range(N):
    a = A[i]
    if a < Pizz[I]:
        p = Pizz[I]
        p1 = p - a
        Pizz.pop(I)
        Pizz.append(a)
        Pizz.append(p1)
        I += 1
    
    elif a > sum(Pizz[I:]):
        a1 = a - Pizz[-1]
        if a1 > 359:
            a1 = a1 % 360
        I = 0
        for i2 in range(500):
            if a1 < Pizz[i2]:
                p1 = (Pizz[i2]) - a1
                Pizz.pop(I)
                Pizz.insert(i2,a1)
                Pizz.insert((i2 + 1),p1)
                break
            I += 1
            a1 = a1 - (Pizz[i2])
    
    else:
        I += 1


print(max(Pizz))