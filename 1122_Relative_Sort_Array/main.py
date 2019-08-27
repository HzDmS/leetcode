class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hashmap = {}
        for i, n in enumerate(arr2):
            hashmap[n] = i
        
        def func(num):
            return (0, hashmap[num]) if num in hashmap else (1, num)
        
        return sorted(arr1, key=func)
