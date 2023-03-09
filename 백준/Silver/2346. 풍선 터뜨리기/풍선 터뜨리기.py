import sys
from collections import deque

n = int(sys.stdin.readline())

deq = deque(enumerate(map(int, sys.stdin.readline().split()), start=1))
for i in range(n):
    p = deq.popleft() # pop(0)과 같은 결과를 가져오지만, pop(0)보다 더 빠르다
    print(p[0], end=' ')
    if p[1] > 0:
        deq.rotate(-(p[1] - 1)) # popleft된 1칸을 제외하고 시계 반대방향으로 회전
    else:
        deq.rotate(-p[1]) # 시계 방향으로 회전