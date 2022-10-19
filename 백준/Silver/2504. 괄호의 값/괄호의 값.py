s = list(input())
stack = []

for i in s:
    if i in ['(', '[']: # 여는 괄호는 전부 스택에 저장
        stack.append(i)
    elif i == ')':  # 닫는 괄호가 ')'인 경우
        tmp = 0
        while True:
            if not stack:
                print(0)
                exit()
            if stack and stack[-1] == '(': # 올바른 괄호 짝짓기 성공
                stack.pop()
                if tmp == 0:    # 연산이 진행중이던 게 없으면 그냥 2 ex. ()
                    stack.append(2)
                else:   # (()) 같은 케이스
                    stack.append(2 * tmp)
                break
            elif stack and stack[-1] == '[':    # 올바르지 않은 괄호
                print(0)
                exit()
            else:
                tmp += int(stack.pop())

    elif i == ']':  # 닫는 괄호가 ']'인 경우
        tmp = 0

        while True:
            if not stack:
                print(0)
                exit()
            if stack and stack[-1] == '[':
                stack.pop()
                if tmp == 0:
                    stack.append(3)
                else:
                    stack.append(3 * tmp)
                break
            elif stack and stack[-1] == '(':
                print(0)
                exit()
            else:
                tmp += int(stack.pop())

for i in stack:
    if i in ['(', ')', '[', ']']:   # 짝짓는 걸 끝마쳤는데 스택에 괄호가 남아있다면 올바르지 않은 괄호
        print(0)
        exit()
else:
    print(sum(stack))