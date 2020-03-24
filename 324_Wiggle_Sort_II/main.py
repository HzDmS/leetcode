class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k = (n - 1) // 2
        mid = self.find_kth(nums, 0, n - 1, k)
        
        def get_index(i):
            if i <= k:
                return n - 1 - i * 2 - (n + 1) % 2
            i -= k + 1
            return n - 1 - i * 2 - n % 2
        
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        left, i, right = 0, 0, n - 1
        while i <= right:
            if nums[get_index(i)] < mid:
                swap(nums, get_index(i), get_index(left))
                left += 1
                i += 1
            elif nums[get_index(i)] == mid:
                i += 1
            else:
                swap(nums, get_index(right), get_index(i))
                right -= 1
        
    def find_kth(self, nums, start, end, k):
        left, right = start, end
        mid = nums[(left + right) // 2]
        
        while left <= right:
            while left <= right and nums[left] < mid:
                left += 1
            while left <= right and nums[right] > mid:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        if k <= right:
            return self.find_kth(nums, start, right, k)
        elif k >= left:
            return self.find_kth(nums, left, end, k)
        else:
            return nums[k]

