n = int(input())
h_list = [int(input()) for _ in range(n)]
left_cnt = right_cnt = 0
left_max = right_max = 0
for e in h_list:
    if e > left_max:
        left_max = e
        left_cnt += 1
for e in h_list[::-1]:
    if e > right_max:
        right_max = e
        right_cnt += 1
print(left_cnt)
print(right_cnt)