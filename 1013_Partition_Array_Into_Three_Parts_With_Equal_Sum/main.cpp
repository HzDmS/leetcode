class Solution {
public:
    
    // time complexity: O(n)
    // space complexity: O(1)
    bool canThreePartsEqualSum(vector<int>& A) {
        int n = A.size();
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += A[i];
        }
        
        int count = 0;
        int cur = 0;
        for (int i = 0; i < n; i++) {
            cur += A[i];
            if (cur == sum / 3) {
                count++;
                cur = 0;
            }
        }
        return count == 3;
    }
    
//     // time complexity: O(n^2)
//     // space complexity: O(n)
//     bool canThreePartsEqualSum(vector<int>& A) {
//         int n = A.size();
//         int sum = 0;
//         vector<int> frontSum(n - 2, 0), endSum(n - 2, 0);
//         for (int i = 0; i < n; i++) {
//             sum += A[i];
//         }
        
//         frontSum[0] = A[0];
//         for (int i = 1; i < n - 2; i++) {
//             frontSum[i] = frontSum[i - 1] + A[i];
//             endSum[i] = sum - frontSum[i] - A[i + 1];
//         }
        
//         for (int i = 0; i < n - 2; i++) {
//             if (frontSum[i] == sum / 3) {
//                 for (int j = i; j < n - 2; j++) {
//                     if (endSum[j] == sum / 3)
//                         return true;
//                 }
//             }
//         }
//         return false;
//     }
};
