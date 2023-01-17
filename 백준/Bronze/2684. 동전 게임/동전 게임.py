n = int(input())
coin = [input() for _ in range(n)]
for e in coin:
    test = {'TTT':0, 'TTH':0, 'THT':0, 'THH':0, 'HTT':0, 'HTH':0, 'HHT':0, 'HHH':0}
    for i in range(38):
        test[e[i:i+3]] += 1
    for v in test.values():
        print(v, end = ' ')
    print()