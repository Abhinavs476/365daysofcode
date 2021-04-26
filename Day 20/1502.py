''' Given an array of numbers arr. A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false. '''

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        arr.sort()
        dif = arr[1] - arr[0]
        lent = len(arr) -1 
        arr.append(0)
        for i in range(0,lent):
            x = arr[i+1] - arr[i]
            if(x != dif):
                return 0
        return 1
        
''' Link: https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/ '''
