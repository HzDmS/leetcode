class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        int end = days.back();
        int n = end + 1;
        int m = costs.size();
        vector<int> paths(n, 0);
        unordered_set<int> s;
        
        for (int d : days) {
            s.insert(d);
        }
        
        for (int i = days.front(); i < n; i++) {
            if (s.find(i) == s.end()) {
                paths[i] = paths[i - 1];
            } else {
                paths[i] = min({paths[i - 1] + costs[0],
                                paths[i >= 7 ? i - 7 : 0] + costs[1],
                                paths[i >= 30 ? i - 30 : 0] + costs[2]});
            }
        }
        return paths.back();
    }
};