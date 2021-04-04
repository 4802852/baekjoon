from collections import Counter

N = int(input())
lst = sorted(list(map(int, input().split()))) # 정렬
M = int(input())
card = list(map(int, input().split()))


counter = Counter(lst)

print(' '.join(str(counter[c]) if c in counter else '0' for c in card))