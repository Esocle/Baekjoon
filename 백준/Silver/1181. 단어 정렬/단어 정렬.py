n = int(input())
words = [input() for _ in range(n)]
words = list(set(words))
words.sort()
words.sort(key=len)
for e in words:
    print(e)