temp = input()
temp = temp.split(" ")
answer = [1, 1, 2, 2, 2, 8]
for a, b in zip(temp, answer):
    a = int(a)
    c = b - a
    print(c, end=" ")