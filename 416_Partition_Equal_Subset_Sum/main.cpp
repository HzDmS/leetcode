class Solution {
public:
    bool canPartition(vector<int>& nums) {
        
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum & 1)
            return false;
        sum /= 2;
        
        vector<int> dp(sum + 1, 0);
        
        dp[0] = 1;
        
        for (auto num : nums) {
            for (int i = sum; i >= num; i--) {
                dp[i] = dp[i] | dp[i - num]; 
            }
        }
        
        return dp[sum];
        
    }
    
    
    // DFS exceeds the time limit! 
    
    // void dfs(vector<int>& nums, int i, int left, int right, bool& res) {
    //     if (res) return;
    //     if (i == nums.size()) {
    //         if (left == right) res = true;
    //         return;
    //     }
    //     dfs(nums, i + 1, left + nums[i], right, res);
    //     dfs(nums, i + 1, left, right + nums[i], res);
    // }
    
};
