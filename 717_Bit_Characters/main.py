class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        cur = 0
        while cur < len(bits) - 1:
            if bits[cur] == 1:
                cur = cur + 2
            else:
                cur += 1
        return cur == len(bits) - 1
