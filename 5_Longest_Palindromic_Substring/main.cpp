class Solution {
public:
    
    string longestPalindrome(string s) {
        
        int n = s.size();
        int start = 0, len = 0;
        vector<vector<int>> dp(n, vector<int>(n, 1));
        
        for (int i = n - 2; i >= 0; i--) {
            for (int j = i + 1; j <= n - 1; j++) {
                dp[i][j] = (s[i] == s[j]) ? dp[i + 1][j - 1] : 0;
                if (dp[i][j] && j - i > len) {
                    start = i;
                    len = j - i;
                }
            }
        }
        
        return s.substr(start, len + 1);
        
    }
    
//     string longestPalindrome(string s) {
        
//         int n = s.size();
//         int start = n, max = 0;
//         vector<vector<int>> dp(n, vector<int>(n, 0));
        
//         for (int i = n - 1; i >= 0; i--) {
//             for (int j = i; j <= n - 1; j++) {
//                 if ((i == j) ||
//                     (j == (i + 1) && s[i] == s[j]) ||
//                     (j > i + 1 && dp[i + 1][j - 1] == 1 && s[i] == s[j])) {
//                     dp[i][j] = 1;
//                     if (j - i >= max) {
//                         max = j - i;
//                         start = i;
//                     }
//                 }
//             }
//         }
        
//         return s.substr(start, max + 1);
        
//     }
};
