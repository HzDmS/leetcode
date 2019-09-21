from random import randint


class Solution:

    def __init__(self, nums: List[int]):
        self.org = nums
        self.cur = list(nums)
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.cur = self.org
        self.org = list(self.org)
        return self.cur
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.cur)):
            j = randint(i, len(self.cur) - 1)
            self.cur[i], self.cur[j] = self.cur[j], self.cur[i]
        return self.cur


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
