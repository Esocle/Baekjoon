n = int(input())
nums = [input() for _ in range(n)]
nums.sort(key=len)
nums = sorted(nums, key=lambda s: (len(s), sum([int(i) for i in s if type(i)== int or i.isdigit()]), s))   
for n in nums:
    print(n)