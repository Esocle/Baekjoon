number = list((input()))
number.sort(reverse=True)
final = ''
for e in number:
    final += e
print(final)