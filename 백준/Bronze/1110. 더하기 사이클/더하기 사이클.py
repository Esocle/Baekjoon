cnt = 0
basic = int(input())
num = basic
while True:
    num = (num//10 + num%10)%10 + (num%10 * 10)
    cnt += 1
    if num == basic:
        break
print(cnt)