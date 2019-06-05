class Solution {
public:
    
    // stack solution
    // time complexity: O(n)
    // space complexity: O(1)
    string removeOuterParentheses(string S) {
        int count = 0;
        string res = "";
        for(int i = 0; i < S.size(); i++) {
            char cur = S[i];
            if(count == 0) count++;
            else {
                if (cur == '(') {
                    count++;
                } else {
                    count--;
                }
                if (count > 0 ) res.push_back(cur);
            }
        }
        return res;
    }
    
    // stack solution
    //time complexity: O(n)
    //space complexity: O(n) worst case
    // string removeOuterParentheses(string S) {
    //     stack<char> s;
    //     string res = "";
    //     for(int i = 0; i < S.size(); i++) {
    //         char cur = S[i];
    //         if(s.size() == 0) s.push(cur);
    //         else {
    //             if (cur == '(') {
    //                 s.push(cur);
    //             } else {
    //                 s.pop();
    //             }
    //             if (s.size() > 0 ) res.push_back(cur);
    //         }
    //     }
    //     return res;
    // }
};
