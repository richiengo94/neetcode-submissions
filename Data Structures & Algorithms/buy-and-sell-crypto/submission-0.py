class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result: int = 0
        l_ptr: int = 0
        r_ptr: int = 0

        while r_ptr < len(prices):
            if prices[r_ptr] > prices[l_ptr]:
                result = max(prices[r_ptr] - prices[l_ptr], result)
            else:
                l_ptr = r_ptr
            
            r_ptr += 1
        
        return result