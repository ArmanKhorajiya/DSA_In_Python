# class Solution(object):
#     def maxProfit(self,prices):
#         minimum=prices[0]
#         profit=0

#         for i in range(len(prices)):

#             if prices[i]<minimum:
#                 minimum=prices[i]

#             current_profit=prices[i]-minimum

#             if current_profit>profit:
#                 profit=current_profit

#         return profit
#     print(maxProfit(0,[6,4,7,2,9]))