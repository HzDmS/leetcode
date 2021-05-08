from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return sum(map(lambda _: _ * (_ - 1) // 2, counter.values()))

