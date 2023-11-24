def solution(today, terms, privacies):
    rules = {}
    answer = []
    today_list = list(map(int, today.split('.')))
    
    for t in terms:
        a, b = t.split()
        rules[a] = int(b)*28
        
    for i in range(len(privacies)):
        date, r = privacies[i].split()
        date_list = list(map(int, date.split('.')))
        year = (today_list[0] - date_list[0])*336
        month = (today_list[1] - date_list[1])*28
        day = today_list[2] - date_list[2]
        total = year + month + day
        if rules[r] <= total:
            answer.append(i+1)
    return answer