while True:
    n = int(input())
    if n == 0: break
    test = [input() for _ in range(n)]
    
    print(sorted(test, key=lambda x: x.lower())[0])