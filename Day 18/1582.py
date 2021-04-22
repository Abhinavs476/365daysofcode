''' Given a string s and an integer array indices of the same length.
The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
Return the shuffled string. '''

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = str()
        for ind in range(len(indices)):
            result += s[indices.index(ind)]
        return result
''' Link:https://leetcode.com/problems/shuffle-string/ '''
