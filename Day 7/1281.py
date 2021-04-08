''' Given an integer number n, return the difference between the product of its digits and the sum of its digits. '''

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        prod = 1
        sumi = 0
        while n>0:
            digit = n %10
            prod = prod * digit
            sumi =  sumi + digit
            n = n//10
        
        return prod - sumi
      
''' Link:https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/ '''
