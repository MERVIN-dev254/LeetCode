class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        fin_str = ''
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return fin_str
                
            fin_str += strs[0][i]
                    
        return fin_str