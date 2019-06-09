class Solution {
public:
    vector<int> addToArrayForm(vector<int>& A, int K) {
        vector<int> k;
        while (K > 0) {
            k.push_back(K % 10);
            K /= 10;
        }
        
        reverse(k.begin(), k.end());
        
        vector<int> res;
        int c = 0;
        int d = 0;
        int m = k.size(), n = A.size();
        for (int i = 0; i < max(m, n); i++) {
            if (i >= m) 
                d = A[n - i - 1] + c;
            else if (i >= n)
                d = k[ m - i - 1] + c;
            else
                d = A[n - i - 1] + k[m - i - 1] + c;
            c = d / 10;
            d = d % 10;
            res.push_back(d);
        }
        
        if (c != 0)
            res.push_back(c);
        reverse(res.begin(), res.end());
        return res;
    }
};
