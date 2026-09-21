# class Solution(object):
#     def productExceptSelf(self,nums):

#         product=1
#         left=[1]*len(nums)

#         for i in range(len(nums)):
#             left[i]=product
#             product=product*nums[i]

#         product=1
#         right=[1]*len(nums)

#         for i in range(len(nums)-1,-1,-1):
#             right[i]=product
#             product=product*nums[i]

#         answer=[]
#         for i in range(len(nums)):
#             answer.append(left[i]*right[i])
#         return answer
# solution=Solution()
# print(solution.productExceptSelf([1,2,3,4]))