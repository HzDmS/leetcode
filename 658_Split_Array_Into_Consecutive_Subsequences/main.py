from collections import defaultdict

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = defaultdict(int)
        tails = defaultdict(int)
        
        for num in nums:
            freq[num] += 1
            tails[num] = 0
        
        for num in nums:
            if freq[num] == 0:
                continue

            if num - 1 in tails and tails[num - 1] > 0:
                tails[num - 1] -= 1
                tails[num] += 1
            elif num + 1 in freq and num + 2 in freq and freq[num + 1] > 0 and freq[num + 2] > 0:
                tails[num + 2] += 1
                freq[num + 1] -= 1
                freq[num + 2] -= 1
            else:
                return False
            freq[num] -= 1
        return True
        
