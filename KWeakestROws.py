class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        lis = []
        for index, li in enumerate(mat):
            cand = (sum(li), index)
            lis.append(cand) #normal list of tuples
            
        lis.sort() #sorted list: first with sum, if sum is equal, sorted with index
            
        return [i[1] for i in lis[:k]] #slicing the list upto index k-1
                
                
        