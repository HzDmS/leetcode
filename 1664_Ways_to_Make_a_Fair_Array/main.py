class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        left_sum = [[0, 0] for _ in range(n)] 
        for i in range(1, n):
            if i % 2 == 0:
                left_sum[i][0] = left_sum[i - 1][0] 
                left_sum[i][1] = left_sum[i - 1][1] + nums[i - 1]
            else:
                left_sum[i][0] = left_sum[i - 1][0] + nums[i - 1]
                left_sum[i][1] = left_sum[i - 1][1] 
        right_sum = [[0, 0] for _ in range(n)]
        for i in range(n - 1, 0, -1):
            if i % 2 == 1:
                right_sum[i - 1][0] = right_sum[i][0] 
                right_sum[i - 1][1] = right_sum[i][1] + nums[i]
            else:
                right_sum[i - 1][0] = right_sum[i][0] + nums[i]
                right_sum[i - 1][1] = right_sum[i][1] 
        
        cnt = 0
        
        for i in range(n):
            even_sum = left_sum[i][0] + right_sum[i][1]
            odd_sum = left_sum[i][1] + right_sum[i][0]
            if even_sum == odd_sum:
                cnt += 1
        return cnt

