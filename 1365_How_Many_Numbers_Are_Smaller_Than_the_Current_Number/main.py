from collections import Counter


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        cur = 0
        for key in sorted(counter.keys()):
            counter[key], cur = cur, cur + counter[key]
        return [counter[key] for key in nums]
