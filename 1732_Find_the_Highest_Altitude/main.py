class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = max(0, gain[0])
        for i in range(1, len(gain)):
            gain[i] += gain[i - 1]
            highest = max(highest, gain[i])
        return highest

