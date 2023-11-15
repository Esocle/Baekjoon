def solution(clothes):
    hash_map = {}
    for c in clothes:
        hash_map[c[1]] = hash_map.get(c[1], 0) + 1
    answer = 1
    for h in hash_map:
        answer *= (hash_map[h]+1)
    return answer - 1