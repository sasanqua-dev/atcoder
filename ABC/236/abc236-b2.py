from collections import Counter
t_number = input()
card = list(map(int,input().split()))
print([r_card for r_card in card if not card.count(r_card) == 4][0])