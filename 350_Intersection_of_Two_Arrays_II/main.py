from collections import defaultdict


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        hashmap = defaultdict(int)
        for i in nums1:
            hashmap[i] += 1
        for j in nums2:
            if hashmap[j] > 0:
                ans.append(j)
                hashmap[j] -= 1
        return ans
