''' Given an integer n and an integer start.
Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.
Return the bitwise XOR of all elements of nums. '''

class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        xo = 0
        nums = [0]*n
        for i in range(n):
            nums[i] = start + i + i
            xo = xo^nums[i]
        return xo
      
''' Link: https://leetcode.com/problems/xor-operation-in-an-array/ '''
