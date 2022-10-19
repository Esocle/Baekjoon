people, price = map(int, input().split())
grade = [e for e in map(int, input().split())]
grade.sort()
print(grade[-price])