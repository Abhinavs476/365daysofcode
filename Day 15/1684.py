''' You are given a string allowed consisting of distinct characters and an array of strings words.
A string is consistent if all characters in the string appear in the string allowed.
Return the number of consistent strings in the array words. '''

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c = 0
        for word in words:
            if len(set(word) - set(allowed)) == 0:
                c += 1
        return c
      
''' Link: https://leetcode.com/problems/count-the-number-of-consistent-strings/ '''
