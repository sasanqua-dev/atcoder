t_number = input()
card = list(map(int,input().split()))
for i in range(int(t_number)):
    if not card.count(i+1) == 4:
        print(i+1)
        break