temp = int(input())
l = [int(e) for e in input().split(" ")]
high = max(l)
for i in range(len(l)):
    l[i] = l[i]/high*100
print(sum(l)/temp)