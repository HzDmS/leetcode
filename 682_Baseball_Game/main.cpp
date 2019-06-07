class Solution {
public:
    int calPoints(vector<string>& ops) {
        int res = 0;
        vector<int> scores;
        for (int i = 0; i < ops.size(); i++) {
            string cur = ops[i];
            if (cur == "D") scores.push_back(2 * scores.back());
            else if (cur == "C") scores.pop_back();
            else if (cur == "+") scores.push_back(
                scores[scores.size() - 1] + scores[scores.size() - 2]);
            else scores.push_back(stoi(cur));
        }
        
        for (int i : scores) {
            res += i;
        }
        
        return res;
        
    }
};
