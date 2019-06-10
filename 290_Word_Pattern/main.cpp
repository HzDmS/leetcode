class Solution {
public:
    bool wordPattern(string pattern, string str) {
        
        map<char, string> m;
        map<string, char> n;
        string cur = "";
        vector<string> vec;
        for (auto c: str) {
            if (c == ' ' && cur.size() != 0) {
                vec.push_back(cur);
                cur = "";
            } else {
                cur += c;
            }
        }
        vec.push_back(cur);
        
        if (vec.size() != pattern.size())
            return false;
        
        for (int i = 0; i < pattern.size(); i++) {
            if (m.find(pattern[i]) == m.end())
                m[pattern[i]] = vec[i];
            if (n.find(vec[i]) == n.end())
                n[vec[i]] = pattern[i];
            if ((m[pattern[i]] != vec[i]) || (n[vec[i]] != pattern[i]))
                return false;
        }
        return true;
    }
};
