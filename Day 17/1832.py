''' A pangram is a sentence where every letter of the English alphabet appears at least once.
Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise. '''

import string
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet_set = "abcdefghijklmnopqrstuvwxyz"
        for char in alphabet_set:
            if char not in sentence:
                return False
        return True


''' Link:https://leetcode.com/problems/check-if-the-sentence-is-pangram/ '''
