class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res;
        stack<int> st;
        map<int, int> m;
        for (int i = nums2.size() - 1; i >= 0; i--) {
            while (!st.empty()) {
                if (st.top() <= nums2[i])
                    st.pop();
                else
                    break;
            }
            if (!st.empty())
                m[nums2[i]] = st.top();
            st.push(nums2[i]);
        }
        
        for (int i = 0; i < nums1.size(); i++) {
            if (m.find(nums1[i]) != m.end())
                res.push_back(m[nums1[i]]);
            else
                res.push_back(-1);
        }
        return res;
    }
};
