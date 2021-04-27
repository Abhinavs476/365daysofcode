''' You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string. '''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        for i in range(min(len(word1), len(word2))):
            result.extend([word1[i], word2[i]])
                       
        if len(word1) < len(word2):
            long = word2
        else:
            long = word1
                       
        result.extend(long[i+1:])
                       
        return "".join(result)

''' Link: https://leetcode.com/problems/merge-strings-alternately/ '''
