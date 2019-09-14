class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited, hashset = {}, set(nums)
        
        maximum = 0
        def check(i):
            if i in visited:
                return visited[i]
            if i + 1 in hashset:
                cnt = check(i + 1) + 1
                visited[i] = cnt
                return cnt
            else:
                return 1
        
        for num in nums:
            maximum = max(check(num), maximum)
        
        return maximum

