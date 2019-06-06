class Solution {
public:

//string itself can be viewed as a stack
//time complexity: O(n)
//space complexity: O(n) worst
//     string removeDuplicates(string S) {
        
//         string res = "";

//         for (auto c : S) {
//             if (res.back() != c) res.push_back(c);
//             else res.pop_back();
//         }
        
//         return res;
        
//     }
    
    //extra stack
    //time complexity: O(n)
    //space complexity: O(n)
    //this solution has a larger factor than the one above
    string removeDuplicates(string S) {
        
        string res = "";
        
        stack<char> st;
        for (auto c : S) {
            if (st.empty()) st.push(c);
            else{
                if (st.top() == c) st.pop();
                else st.push(c);
            }
        }
        
        while(!st.empty()) {
            char c = st.top();
            res.push_back(c);
            st.pop();
        }
        
        reverse(res.begin(), res.end());
        
        return res;
        
    }
};
