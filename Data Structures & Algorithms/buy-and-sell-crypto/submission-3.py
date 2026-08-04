class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        slow, fast = 0, 1
        maxP = 0
        while fast < len(prices):
            if prices[slow] < prices[fast]:
                profit = prices[fast] - prices[slow]
                maxP = max(maxP, profit)
            else:
                slow = fast
            fast += 1
        return maxP