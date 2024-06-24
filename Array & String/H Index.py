from typing import List


class Solution:
    def hIndex(self, citation:List[int]) -> int:
        n = len(citation)
        temp = [0 for i in range(len(citation) + 1)]
        for i,v in enumerate(citation):
            if v > n:
                temp[n] += 1
            else:
                temp[v] += 1
        total = 0
        for i in range(n, -1, -1):
            total += 1
            if total >= i:
                return i
    
    
solution = Solution()
citation = [3,0,6,1,5]
print(solution.hIndex(citation))