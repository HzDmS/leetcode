class Solution {
public:
    vector<int> shortestToChar(string S, char C) {
        vector<int> points;
        int n = S.size();
        vector<int> res(n, 0);
        points.push_back(INT_MIN / 2);
        for (int i = 0; i < n; i++) {
            if (S[i] == C) points.push_back(i);
        }
        points.push_back(INT_MAX / 2);

        int m = points.size();

        for (int i = 0, j = 0; i < n; i++) {
            if (i == points[j + 1]) {
                j++;
                continue;
            }
            res[i] = min(i - points[j], points[j + 1] - i);
        }

        return res;

}
//     vector<int> shortestToChar(string S, char C) {
//         vector<int> points;
//         int n = S.size();
//         vector<int> res(n, 0);
//         for (int i = 0; i < n; i++) {
//             if (S[i] == C) points.push_back(i);
//         }
        
//         int m = points.size();
        
//         for (int i = 0; i < points[0]; i++) {
//             res[i] = points[0] - i;
//         }
        
//         for (int i = points[0] + 1, j = 0; i < points[m - 1]; i++) {
//             if (i == points[j + 1]) {
//                 j++;
//                 continue;
//             }
//             res[i] = min(i - points[j], points[j + 1] - i);
//         }
        
//         for (int i = points[m - 1] + 1; i < n; i++) {
//             res[i] = i - points[m - 1];
//         }
        
//         return res;
        
//     }
};
