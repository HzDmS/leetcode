class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        prev = -1
        for i, num in enumerate(nums):
            if num == target:
                distance = i - start if start <= i else start - i
                if prev < 0 or prev >= distance:
                    prev = distance
                else:
                    return prev
        return prev

