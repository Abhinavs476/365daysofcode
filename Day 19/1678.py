''' You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. 
The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al".
The interpreted strings are then concatenated in the original order.
Given the string command, return the Goal Parser's interpretation of command. '''

class Solution:
    def interpret(self, command: str) -> str:
        output = ''
        for i in range(len(command)):
            if command[i] == "G":
                output += "G"
            elif command[i] == "(":
                if command[i+1] == 'a':
                    output += "al"
                elif command[i+1] == ")":
                    output += "o"
                else:
                    pass
            else:
                pass
        return output
        
''' Link: https://leetcode.com/problems/goal-parser-interpretation/ '''
