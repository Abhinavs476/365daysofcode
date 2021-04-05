''' Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn]. '''

class Solution(object):
    def shuffle(self, nums, n):
        l=[0]*len(nums)
        j=0
        for i in range(0,n):
            l[j]=nums[i]
            l[j+1]=nums[i+n]
            j=j+2
        return l
      
''' Link: https://leetcode.com/problems/shuffle-the-array/ '''
