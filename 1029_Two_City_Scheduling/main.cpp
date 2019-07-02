class Solution {
public:
    
    static bool cmp(vector<int> a, vector<int> b) {
        return (a[0] - a[1]) < (b[0] - b[1]);
    }
    
    int twoCitySchedCost(vector<vector<int>>& costs) {
        int sum = 0;
        int n = costs.size();
        sort(costs.begin(), costs.end(), cmp);
        for (int i = 0; i < n; i++) {
            sum += i < n / 2 ? costs[i][0] : costs[i][1];
        }
        
        return sum;
        
    }
};
