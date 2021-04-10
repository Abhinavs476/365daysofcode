''' Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
A string is represented by an array if the array elements concatenated in order forms the string. '''
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        lent1 = len(word1)
        strin1 = ""
        lent2 = len(word2)
        strin2 = ""
        for i in range(lent1):
            strin1 = strin1 + word1[i]
        for j in range(lent2):
            strin2 = strin2 + word2[j]
        if(strin1 == strin2):
            return 1
        else:
            return 0
''' Link: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/ '''
