class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        e = {}
        for i in ransomNote:
            d[i] = ransomNote.count(i)
        for i in magazine:
            e[i] = magazine.count(i)
            
#         rans_set = set(d)
#         maga_set = set(e)
        
        for k in d.keys():
            if d[k] > e[k]:
                return False
            return True
                    
