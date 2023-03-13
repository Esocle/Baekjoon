import sys
input = sys.stdin.readline
stack = []

n = int(input())
for _ in range(n):
    ts = input().strip()

    if 'push' in ts:
        _, tn = ts.split()
        tn = int(tn)
        stack.append(tn)
    elif ts == 'pop':
        try: 
            p = stack.pop()
            print(p)
        except: print(-1)
    elif ts == 'size':
        print(len(stack))
    elif ts == 'empty':
        if len(stack) == 0: print(1)
        else: print(0)
    else:
        try: print(stack[-1])
        except: print(-1)