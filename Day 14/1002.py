''' Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).
For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.
You may return the answer in any order. '''

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        d = dict()
        
        for ch in A[0]:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
                
        for k in d:
            for word in A[1:]:
                cnt = word.count(k)
                if cnt < d[k]:
                    d[k] = cnt
                    
        commonChars = []
        
        for k in d:
            if d[k] > 0:
                commonChars += [k] * d[k]
                
        return commonChars

''' Link: https://leetcode.com/problems/find-common-characters/ '''
