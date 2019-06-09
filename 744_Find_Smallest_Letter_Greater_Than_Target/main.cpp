class Solution {
public:
    // time complexity: O(n)
    // space complexity: O(1)
    char nextGreatestLetter(vector<char>& letters, char target) {
        char res = letters.front();
        for (auto letter : letters) {
            if (letter > target) {
                res = letter;
                break;
            }
        }
        return res;
    }
};
