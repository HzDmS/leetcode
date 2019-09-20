class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        count = 0
        start = 0
        while count < n:
            cur = start
            prev = nums[start]
            while True:
                nex = (cur + k) % n
                tmp = nums[nex]
                nums[nex] = prev
                prev = tmp
                cur = nex
                count += 1
                if start == cur:
                    break
            start += 1
           
