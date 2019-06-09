class Solution {
public:
    //time complexity: O(1)
    //space comlexity: O(1)
    // general case: 
    //     minimum: directly move two stones to the right position.
    //     maximum: move one step at each time.
    vector<int> numMovesStones(int a, int b, int c) {
        vector<int> res({0, 0});
        int dist[3] = {abs(a - b), abs(b - c), abs(a - c)};
        sort(dist, dist + 3, comp);
        int x = dist[0] - 1, y = dist[1] - 1;
        if (x == 0){
            if (y == 0)
                res[0] = 0;
            else
                res[0] = 1;
        }
        else if (x == 1)
            res[0] = 1;
        else
            res[0] = 2;
        
        res[1] = x + y;
        return res;
    }
    
    static bool comp (int& a, int& b) {
        return a < b;
    }
};
