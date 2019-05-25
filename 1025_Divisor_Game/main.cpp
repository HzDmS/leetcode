class Solution {
public:
    
    bool divisorGame(int N) {
        
        //dynamic programming
        //time complexity: O(N ^ 2)
        //space complexity: O(N)
        
        vector<bool> dp(N + 1, false);
        
        for (int i = 2; i <= N; i++) {
            for (int j = 1; j < i; j++) {
                if ((i % j) == 0 && dp[i - j] == false) {
                    dp[i] = true;
                }
            }
        }
        
        return dp[N];
        
    }
    
//time complexity: O(1)
//space complexity: O(1)
//     bool divisorGame(int N) {
        
//         return !(N & 1);
        
//     }
};
