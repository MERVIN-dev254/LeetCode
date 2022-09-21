class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x += 2 * (0 - x)
            y = str(x)
            z = y[::-1]
            b = 0 - int(z)
            return b
        if x > 0:
            y = str(x)
            z = y[::-1]
            b = int(z)
            return b
        
        
            
        
        
        
        
        