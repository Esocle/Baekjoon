import sys

while True:
    try:
        word = str(sys.stdin.readline().rstrip("\n"))
        print(word)
        if word == "":
            break
    except:
        break