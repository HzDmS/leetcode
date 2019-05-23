class Solution {
public:
    vector<string> commonChars(vector<string>& A) {
        
        vector<string> res;
        
        vector<int> overall(26, 0);
        for (char i : A[0]) {
            overall[i - 'a']++;
        }
        
        for (int i = 1; i < A.size(); i++) {
            vector<int> current(26, 0);
            for (char j : A[i]) {
                current[j - 'a']++;
            }
            
            for (int k = 0; k < overall.size(); k++) {
                overall[k] = min(current[k], overall[k]);
            }
        }
        
        for (int i = 0; i < overall.size(); i++) {
            while(overall[i] > 0) {
                res.push_back(string(1, 'a' + i));
                overall[i]--;
            }
        }
        
        return res;
        
    }
};
