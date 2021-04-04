''' Given the array candies and the integer extraCandies, where candies[i] represents the number of candiesthat the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number 
of candies among them. Notice that multiple kids can have the greatest number of candies. '''

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        lent = len(candies)
        candy = [1] * lent
        maxi = 0
        for i in range(lent):
            if candies[i]>=maxi:
                maxi = candies[i] #works
        for i in range(lent):
            candies[i] = candies[i]+extraCandies
        for i in range(lent):
            if candies[i]<maxi:
                candy[i] = 0
        return candy
      
''' link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/ '''
