from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixSum, hashMap = [0] * n, defaultdict(int)
        cnt = 0
        
        prefixSum[0] = nums[0]
        hashMap[0] = 1

        for i in range(1, n):
            prefixSum[i] = prefixSum[i - 1] + nums[i]
        
        for s in prefixSum:
            if s - k in hashMap:
                cnt += hashMap[s - k]
            hashMap[s] += 1
        
        return cnt

