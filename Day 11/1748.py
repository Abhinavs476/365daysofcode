''' You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
Return the sum of all the unique elements of nums. '''

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        summ=0
        for k,v in d.items():
            if v==1:
                summ+=k
        return summ
      
''' Link: https://leetcode.com/problems/sum-of-unique-elements/ '''
