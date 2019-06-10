class Solution {
public:
    // time complexity: < O(n)
    // space complexity: O(1);
    bool checkPerfectNumber(int num) {
        int sum = 1;
        for (int i = 2; i < num / i; i++) {
            if (num % i == 0) {
                sum = sum + i + num / i;
            }
        }
        
        return num > 1 && sum == num;
    }
};
