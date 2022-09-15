class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        ref = {"I": 1,
               "V": 5,
               "X": 10,
               "L": 50,
               "C": 100,
               "D": 500,
               "M": 1000}
        
        for i in range(len(s)):
            if i + 1 < len(s) and ref[s[i]] < ref[s[i + 1]]:
                num -= ref[s[i]]
            else:
                num += ref[s[i]]
        return num