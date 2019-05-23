class Solution {
public:
    vector<int> sumEvenAfterQueries(vector<int>& A, vector<vector<int>>& queries) {
        int n = A.size();
        vector<int> res;
        int sum = 0;
        
        for (int i = 0; i < n; i++) {
            if (A[i] % 2 == 0) {
                sum += A[i];
            }
        }
        
        for (int i = 0; i < queries.size(); i++) {
            if (!(queries[i][0] & 0x01) && !(A[queries[i][1]] & 0x01)) {
                sum += queries[i][0];
            }
            
            if ((queries[i][0] & 0x01) && (A[queries[i][1]] & 0x01)) {
                sum += (A[queries[i][1]] + queries[i][0]);
            }
            
            if ((queries[i][0] & 0x01) && !(A[queries[i][1]] & 0x01)) {
                sum -= A[queries[i][1]];
            }
            
            A[queries[i][1]] = A[queries[i][1]] + queries[i][0];
            res.push_back(sum);
        }
        return res;
    }
};
