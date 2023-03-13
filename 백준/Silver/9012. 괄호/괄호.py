n = int(input())
for _ in range(n):
    stack = list(input().strip())
    while stack:
        if stack[0] == '(' and stack.count(')'):
            stack.pop(0)
            
            for i in range(len(stack)):
                if stack[i] == ')':
                    stack.pop(i)
                    break
                
        else: break
    
    if stack: print('NO')
    else: print('YES')