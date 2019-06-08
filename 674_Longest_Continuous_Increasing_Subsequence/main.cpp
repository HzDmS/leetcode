class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        
        // two pointers.
        // time complexity: O(n);
        // space complexity: O(1);
        
        if (nums.empty()) return 0;
        
        int start = 0, end = 0, res = 1;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > nums[i - 1]){
                end++;
            }
            else{
                res = max(res, end - start + 1);
                start = i, end = i;
            }
        }
        
        res = max(res, end - start + 1);
        
        return res;
    }
};
