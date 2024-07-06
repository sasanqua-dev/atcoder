def check_substring(s, t):
    for w in range(1, len(s)):
        for c in range(1, w + 1):
            substrings = [s[i:i+w] for i in range(0, len(s), w)]
            concatenated = ''.join([sub[c-1] for sub in substrings if len(sub) >= c])
            if concatenated == t:
                return "Yes"
    return "No"

# 入力の取得
s, t = input().split()
result = check_substring(s, t)
print(result)
