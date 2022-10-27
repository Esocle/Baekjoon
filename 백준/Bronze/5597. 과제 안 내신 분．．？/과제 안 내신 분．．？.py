students = [int(input()) for _ in range(28)]
answer = list(set(range(1, 31)) - set(students))
answer.sort()
print(answer[0])
print(answer[1])