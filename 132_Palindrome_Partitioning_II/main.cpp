class Solution {
public:
    int minCut(string s) {
        int n = s.size();
        vector<vector<bool>> isPalin(n, vector<bool>(n, false));
        for (int i = 0; i < n; i++) {
            isPalin[i][i] = true;
            if (i < n - 1)
                isPalin[i + 1][i] = (s[i] == s[i + 1]);
        }
        
        for (int i = 2; i < n; i++) {
            for (int j = 0; j < i - 1; j++) {
                isPalin[i][j] = (isPalin[i - 1][j + 1] && (s[i] == s[j]));
            }
        }
        
        vector<int> dp(n + 1, -1);
        
        for (int i = 1; i < n + 1; i++) {
            dp[i] = i - 1;
        }
        
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j <= i; j++) {
                if (isPalin[i - 1][j - 1])
                    dp[i] = min(dp[i], dp[j - 1] + 1);
            }
        }
        
        return dp[n];
        
    }
};