class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            b = 0
            return b
        if x < 0:
            x += 2 * (0 - x)
            y = str(x)
            z = y[::-1]
            b = 0 - int(z)
            
            if b < -2**31 or b>2**31:
                b = 0
            return b
        if x > 0:
            y = str(x)
            z = y[::-1]
            b = int(z)
            if b < -2**31 or b>2**31:
                b = 0
            return b
            
        
        
            
        
        
        
        
        