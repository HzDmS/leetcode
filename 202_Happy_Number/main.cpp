class Solution {
public:
    bool isHappy(int n) {
        set<int> showedNums;
        showedNums.insert(n);
        int sum = n;
        while (true) {
            sum = int2sum(sum);
            if (sum == 1)
                return true;
            if (showedNums.count(sum) != 0)
                return false;
            showedNums.insert(sum);
        }
    }
    
    int int2sum(int n) {
        int sum = 0;
        while (n > 0) {
            sum += (n % 10) * (n % 10);
            n /= 10;
        }
        return sum;
    }
};
