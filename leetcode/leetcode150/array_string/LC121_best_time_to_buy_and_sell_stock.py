"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        raise NotImplementedError()
    
class Solution1(Solution):
    def maxProfit(self, prices: List[int]) -> int:
        '''
            sliding window
            find every lowest/highest point for each window
            when reach newer low point, start next window, 
                since it may result in extent new range
            compare each window find max
        '''
        buy = 0
        sell = 1
        max_profit = 0
        while (sell < len(prices)):
            # cur profile could be minus
            cur_profit = prices[sell] - prices[buy]
            # when sell smaller then buy, means find new lower point
            if prices[sell] < prices[buy]:
                # move window start from this new loe point
                buy = sell
            else:
                # otherwise, keep extend current window find max
                max_profit = max(cur_profit, max_profit)
            # move sell point to find overall max
            sell += 1
        return max_profit