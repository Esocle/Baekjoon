import sys
from collections import Counter

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]
nums.sort()
nums_s = Counter(nums).most_common(2)
print(round(sum(nums)/n))
print(nums[n//2])
if len(nums_s) > 1:
    if nums_s[0][1] == nums_s[1][1]:
        print(nums_s[1][0])
    else:
        print(nums_s[0][0])
else:
    print(nums_s[0][0])
print(max(nums)-min(nums))