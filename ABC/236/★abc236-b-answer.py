from collections import Counter
t_number = input()
card = list(map(int,input().split()))
card_count = Counter(card)
print(card_count.most_common()[::-1][0][0])