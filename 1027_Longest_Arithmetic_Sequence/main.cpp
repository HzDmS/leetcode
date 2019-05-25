class Solution {
public:
    
// time complexity: O(n^2)
// space complexity: O(n^2)
    int longestArithSeqLength(vector<int>& A) {
        
        int res = 0;
        int n = A.size();
        vector<map<int, int>> dp(n);
    
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                int diff = A[i] - A[j];
                if (dp[j].find(diff) != dp[j].end()) {
                    dp[i][diff] = dp[j][diff] + 1;
                } else {
                    dp[i][diff] = 2;
                }
                
                res = max(dp[i][diff], res);
                
            }
        }
        return res;
    }
};
