# class Solution(object):
#     def twoSum(self, nums, target):
#         seen = {}

#         for i in range(len(nums)):
#             needed = target - nums[i]

#             if needed in seen:
#                 return [seen[needed], i]

#             seen[nums[i]] = i;
#     # print(twoSum(0,[2,7,11,15],9))
#     # print(twoSum(0,[3,2,4],6))
#     print(twoSum(0,[3,3],6))