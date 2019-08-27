class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        
        hashset = set(B)
        x = (sum(B) - sum(A)) // 2
        
        for a in A:
            if x + a in hashset:
                return [a, x + a]
