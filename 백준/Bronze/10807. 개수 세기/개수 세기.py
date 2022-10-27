n = int(input())
nums = [e for e in map(int, input().split())]
target = int(input())
print(nums.count(target))