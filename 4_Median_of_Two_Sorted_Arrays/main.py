class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        k = (m + n) // 2
        if (m + n) & 1 == 0:
            c1 = self.find(nums1, nums2, k)
            c2 = self.find(nums1, nums2, k + 1)
            return (c1 + c2) * 0.5
        else:
            c = self.find(nums1, nums2, k + 1)
            return c
            
    def find(self, nums1, nums2, k):
        return self.findKthSortedArray(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, k)
    
    def findKthSortedArray(self, nums1, x1, y1, nums2, x2, y2, k):
        m = y1 - x1 + 1
        n = y2 - x2 + 1
        
        if m < n:
            return self.findKthSortedArray(nums2, x2, y2, nums1, x1, y1, k)
        
        if n == 0:
            return nums1[x1 + k - 1]
        
        if k == 1:
            return min(nums1[x1], nums2[x2])
        
        k2 = min(k // 2, n)
        k1 = k - k2
        
        if nums1[x1 + k1 - 1] == nums2[x2 + k2 - 1]:
            return nums1[x1 + k1 - 1]
        elif nums1[x1 + k1 - 1] > nums2[x2 + k2 - 1]:
            return self.findKthSortedArray(nums1, x1, y1, nums2, x2 + k2, y2, k - k2)
        else:
            return self.findKthSortedArray(nums1, x1 + k1, y1, nums2, x2, y2, k - k1)
        
