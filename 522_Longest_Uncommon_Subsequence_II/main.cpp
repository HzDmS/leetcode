class Solution {
public:
    int findLUSlength(vector<string>& strs) {
        int n = strs.size();
        int res = -1;
        sort(strs.begin(), strs.end(), cmp);
        for (int i = 0; i < n; i++) {
            bool flag = false;
            for (int j = 0; j < n && strs[j].size() >= strs[i].size(); j++) {
                if (i == j) continue;
                if (isSubstring(strs[j], strs[i])) {
                    flag = true;
                    break;
                }
            }
            if (!flag)
                return strs[i].size();
        }
        
        return res;
    }
    
    static bool cmp(string& a, string& b) {
        return a.size() > b.size();
    }
    
    bool isSubstring(string& a, string& b) {
        for (int i = 0, j = 0; i < a.size(); i++) {
            if (a[i] == b[j]) j++;
            if (j == b.size())
                return true;
        }
        return false;
    }
    
};
