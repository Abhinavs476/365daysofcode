''' Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums. '''

class Solution(object):
    def runningSum(self, nums):
        lent = len(nums)
        suma = [0] * lent
        for i in range(lent):
            sum1 = 0
            for j in range(i+1):
                sum1 = sum1 + nums[j]
            suma[i] = sum1
        return suma
''' link: https://leetcode.com/problems/running-sum-of-1d-array/ '''
