class Solution {
public:
    
    int cmp(int& a, int& b) {
        if (a > b) return 1;
        else if (a == b) return 0;
        else return -1;
    }
    
    int maxTurbulenceSize(vector<int>& A) {
        int anchor = 0;
        int n = A.size();
        int res = 1;
        
        for (int i = 1; i < n; i++) {
            int flag = cmp(A[i - 1], A[i]);
            if (flag == 0) {
                anchor = i;
            } else {
                if (i == n - 1 || flag * cmp(A[i], A[i + 1]) != -1) {
                    res = max(res, i - anchor + 1);
                    anchor = i;
                }
            }
        }
        return res;
    }
};
