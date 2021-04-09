''' We are given a list nums of integers representing a list compressed with run-length encoding.
Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0). 
For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.
Return the decompressed list. '''

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        lent = len(nums)
        sumi = 0
        for j in range(0,lent,2):
            sumi = sumi + j
        out = []*sumi
        for i in range(0,lent,2):
            l = [nums[i+1]]*nums[i]
            out = out+l
        return out
       
''' https://leetcode.com/problems/decompress-run-length-encoded-list/ '''
