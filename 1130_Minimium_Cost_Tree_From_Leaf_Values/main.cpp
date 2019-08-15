class Solution {
public:
    
    int mctFromLeafValues(vector<int>& arr) {
        int res = 0, n = arr.size();
        vector<int> s {INT_MAX};
        for (auto i : arr) {
            while (i >= s.back()) {
                int mid = s.back();
                s.pop_back();
                res += mid * min(s.back(), i);
            }
            s.push_back(i);
        }
        
        for (int i = 2; i < s.size(); i++) {
            res += s[i] * s[i - 1];
        }
        return res;
    }
    
    // int mctFromLeafValues(vector<int>& arr) {
    //     vector<vector<int>> dp (arr.size(), vector<int>(arr.size(), INT_MAX));
    //     for (int l = 0; l < arr.size(); l++) {
    //         for (int i = 0; i + l < arr.size(); i++) {
    //             if (l == 0) {
    //                 dp[i][i] = arr[i];
    //             } else {
    //                 for (int k = i + 1; k <= i + l; k++) {
    //                     int lmax = 0, rmax = 0;
    //                     for (int j = i; j < k; j++) {
    //                         lmax = max(lmax, arr[j]);
    //                     }
    //                     for (int j = k; j <= i + l; j++) {
    //                         rmax = max(rmax, arr[j]);
    //                     }
    //                     dp[i][i + l] = min(dp[i][i + l], dp[i][k - 1] + dp[k][i + l] + lmax * rmax);
    //                 }
    //             }
    //         }
    //     }
    //     int sum = 0;
    //     for (int i = 0; i < arr.size(); i++) {
    //         sum += arr[i];
    //     }
    //     return dp[0][arr.size() - 1] - sum;
    // }
};
