dwarf = [int(input()) for _ in range(9)]
dwarf.sort()

sum_= sum(dwarf)

for i in range(len(dwarf)):
    for j in range(i+1, len(dwarf)):
        if sum_ - dwarf[i] - dwarf[j] == 100:
            for k in range(len(dwarf)):
                if k == i or k == j:
                    pass
                else:
                    print(dwarf[k])
            exit()