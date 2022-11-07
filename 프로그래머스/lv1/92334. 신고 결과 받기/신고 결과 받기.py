def solution(id_list, report, k):
    report = list(set(report))
    n = len(id_list)
    c = [[] for _ in range(n)]
    d = {}
    for i, id in enumerate(id_list):
        d[id] = i

    for text in report:
        from_id, to_id = text.split()
        i = d[from_id]
        j = d[to_id]
        c[j].append(i)

    answer = [0] * n
    for c_list in c:
        if len(c_list) >= k:
            for from_id in c_list:
                answer[from_id] += 1
    return answer