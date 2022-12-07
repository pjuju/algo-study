# N = int(input())
# nums = []
# for i in range(N):
#     nums.append(int(input()))
#
# for i in range(len(nums)):  # 버블정렬 - 메모리초과;;
#     for j in range(len(nums)):
#         if nums[i] < nums[j]:
#             nums[i], nums[j] = nums[j], nums[i]
#
# for num in nums:
#     print(num)


N = int(input())
nums = []

for _ in range(N):
    nums.append(int(input()))

nums.sort()

for i in range(len(nums)):
    print(nums[i])