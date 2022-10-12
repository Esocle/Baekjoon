sugar = int(input())
cnt = 0
while sugar >= 0:
    if sugar % 5 == 0:      # 0일때, 5의 배수일때
        cnt += sugar//5
        print(cnt)          # 정답 출력
        break
    sugar -= 3
    cnt += 1
else:
    print(-1)