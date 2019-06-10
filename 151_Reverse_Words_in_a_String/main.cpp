class Solution {
public:
    // time complexity: O(n)
    // space complexity: O(n)
    string reverseWords(string s) {
        string cur = "";
        string res = "";
        int n = s.size();
        for (int i = n - 1; i >= 0; i--) {
            if (s[i] == ' ') {
                if (!cur.empty()) {
                    reverse(cur.begin(), cur.end());
                    res += cur;
                    res += " ";
                    cur = "";
                }
            } else{
                cur += s[i];
                if (i == 0) {
                    reverse(cur.begin(), cur.end());
                    res += cur;
                }
            }
        }
        
        if (res.back() == ' ')
            res.pop_back();
        
        return res;
        
    }
    
    // time complexity: O(n)
    // space complexity: O(n)
//     string reverseWords(string s) {
//         stack<string> sta;
//         string cur = "";
//         s += " ";
//         for (auto c : s) {
//             if (c == ' ') {
//                 if (!cur.empty()) {
//                     sta.push(cur);
//                     cur = "";
//                 }
//             } else{
//                 cur += c;
//             }
//         }
//         string res = "";
//         while (!sta.empty()) {
//             res += sta.top();
//             if (sta.size() > 1)
//                 res += " ";
//             sta.pop();
//         }
        
//         return res;
        
//     }
};
