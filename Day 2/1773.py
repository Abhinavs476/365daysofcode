''' You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule. '''

class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
      
        if(ruleKey == 'type'):
            it = 0
        elif(ruleKey == 'color'):
            it = 1
        else:
            it = 2
        le = len(items)
        ret = 0
        for i in range(le):
            if(items[i][it] == ruleValue):
                ret =ret+1
        return ret
    
''' Link: https://leetcode.com/problems/count-items-matching-a-rule/ '''
