def solution(food):
    temp = []
    answer = ''
    num = 0
    for i in range(1, len(food)):
        num += 1
        for _ in range(food[i]//2):
            temp.append(num)
    for e in temp:
        answer += str(e)
    answer += '0'
    num = 0
    for i in range(len(temp)-1, -1, -1):
        answer += str(temp[i])
    print(answer)
    return answer