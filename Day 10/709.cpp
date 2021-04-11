/* Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase. */

class Solution {
public:
    string toLowerCase(string str) {
        string s;
        transform(str.begin(), str.end(), str.begin(), ::tolower);
        return str;
    }
};

// Link: https://leetcode.com/problems/to-lower-case/
