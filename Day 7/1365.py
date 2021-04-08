''' Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array. '''

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        lent = len(nums)
        con = [0]*lent
        for i in range(lent):
            num = nums[i]
            count = 0
            for j in range(lent):
                if nums[j] < num:
                    count = count + 1
            con[i] = count
        
        return con
      
      ''' Link:https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/ '''
