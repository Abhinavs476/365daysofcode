''' You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the ith customer has in the jth bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth. '''

class Solution(object):
    def maximumWealth(self, accounts):      
        len1 = len(accounts)
        s = [0]*len1
        for i in range(len1):
            len2 = len(accounts[i])
            for j in range(len2):
                s[i] = s[i]+accounts[i][j]
        
        maxi = -1
        
        for i in range(len1):
            if s[i] >= maxi:
                maxi = s[i]
        
        return maxi
        
''' link: https://leetcode.com/problems/richest-customer-wealth/ '''
