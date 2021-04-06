''' Given an array of integers nums. A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs. '''

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]==nums[j] and i<j:
                    count+=1
        return count
      
''' Link: https://leetcode.com/problems/number-of-good-pairs/ '''
