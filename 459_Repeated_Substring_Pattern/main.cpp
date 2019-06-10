class Solution {
public:
    // time complexity: O(n ^ 2)
    // space complexity: O(1)
    bool repeatedSubstringPattern(string s) {
        int n = s.size();
        for (int i = 1; i <= n / 2; i++) {
            if (n % i == 0) {
                bool flag = false;
                for (int j = 0; j < n / i - 1; j++) {
                    if (s.substr(j * i, i) != s.substr((j + 1) * i, i)){
                        flag = true;
                        break;
                    }
                }
                if (!flag)
                    return true;
            }
        }
        return false;
    }
};
