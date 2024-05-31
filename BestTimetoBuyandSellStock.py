# BRUTE FORCE
# TC: T: O(n^2) - quadratic/worst S: O(1) - constant/best

def maxProfit(self, prices: List[int]) -> int:
    g_max = 0

    for i in range(len(prices)):
        l_max = prices[i]

        for j in range(i + 1, len(prices)):
            l_max = max(l_max, prices[j])

        g_max = max(g_max, l_max - prices[i])
    return g_max

# OPTIMIZED
# TC: T: O(n) - linear/fair S: O(1) - constant/best

def maxProfit(self, prices: List[int]) -> int:
    buy, sell, max_profit = 0, 1, 0

    while sell < len(prices):
        if prices[buy] < prices[sell]:
            profit = prices[sell] - prices[buy]
            max_profit = max(max_profit, profit)

        else:
            buy = sell
        sell += 1
    return max_profit
