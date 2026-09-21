# class Solution():
#     def maxSubArray(self,nums):
#         current_sum=nums[0]
#         maximum_sum=nums[0]
        
#         for i in range(1,len(nums)):
#             current_sum = max(current_sum + nums[i], nums[i])
#             if current_sum>maximum_sum:
#                 maximum_sum=current_sum
            
#         return maximum_sum
#     print(maxSubArray(0,[1,2,3,4,5]))