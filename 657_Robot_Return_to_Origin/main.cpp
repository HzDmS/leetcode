class Solution {
public:
    bool judgeCircle(string moves) {
        int up = 0, right = 0;
        for (auto move : moves) {
            switch (move){
                case 'U': up++;
                    break;
                case 'D': up--;
                    break;
                case 'R': right++;
                    break;
                case 'L': right--;
                    break;
            }
        }
        if (up == 0 && right == 0)
            return true;
        return false;
    }
};
