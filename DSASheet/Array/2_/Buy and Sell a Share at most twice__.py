from typing import List


class Solution:
    def maxProfit(self, price : List[int]) -> int:
        first_trade = []
        min_buy_price = price[0]
        max_profit_trade_1 = 0
        for i in range(len(price)):
            min_buy_price = min(min_buy_price, price[i])
            max_profit_trade_1 = max(max_profit_trade_1, price[i] - min_buy_price)
            first_trade.append(max_profit_trade_1)
        
        max_sell_price = price[-1]
        max_profit_trade_2 = 0
        for j in range(len(price) - 1, -1, -1):
            max_sell_price = max(price[j], max_sell_price)
            max_profit_trade_2 = max(max_profit_trade_2, max_sell_price - price[j])
            first_trade[j] += max_profit_trade_2
        return max(first_trade)
    
sol = Solution()
price = [10, 22, 5, 75, 65, 80]
price = [2, 30, 15, 10, 8, 25, 80]
print(sol.maxProfit(price))
            
            
            
            
            
        