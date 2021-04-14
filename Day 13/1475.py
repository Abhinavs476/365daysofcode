''' Given the array prices where prices[i] is the price of the ith item in a shop. 
There is a special discount for items in the shop, if you buy the ith item, then you will receive a discount equivalent to prices[j]
where j is the minimum index such that j > i and prices[j] <= prices[i], otherwise, you will not receive any discount at all.
Return an array where the ith element is the final price you will pay for the ith item of the shop considering the special discount. '''

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n=len(prices)
        for i in range(n-1):
            for j in range(i+1,n):
                if prices[j] <= prices[i]:
                    prices[i]-=prices[j]
                    break
        return prices
''' Link: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/ '''
