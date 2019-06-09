class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        vector<string> letters({".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."});
        set<string> s;
        for (auto word : words) {
            string cur = "";
            for (char c : word) {
                cur += letters[c - 'a'];
            }
            s.insert(cur);
        }
        
        return s.size();
    }
};
