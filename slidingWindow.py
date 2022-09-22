class Solution:
    def slidingWindow(arr: List[int], k:int) -> List[int]:
        cur = sum(arr[:k])
        res = [cur]
        
        for i in range(1, len(arr)-k + 1):
            cur -= arr[i - 1]
            cur += arr[i + k - 1]
            res.append(cur)
            
        return res
            
        