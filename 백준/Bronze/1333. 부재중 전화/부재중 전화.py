N, L, D = map(int, input().split())
check = [False] * (N * L + 5 * (N - 1))

for i in range(N):
    s = (L + 5) * i
    for j in range(s, s + L):
        check[j] = True

answer = 0
while answer < len(check):
    if not check[answer]:
        break
    answer += D
print(answer)