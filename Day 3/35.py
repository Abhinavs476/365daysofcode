''' Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order. '''

class Solution(object):
    def searchInsert(self, nums, target):
        lent = len(nums)
        last = lent -1;
        
        if target < nums[0]:
            return 0
        elif target> nums[last]:
            return last +1
        pos = -1
        for i in range(lent):
            if nums[i] == target:
                pos = i;
        if pos != -1:
            return pos
        else:
            for i in range(lent):
                if nums[i]>=target:
                    return i
                  
 ''' link: https://leetcode.com/problems/search-insert-position/ '''
