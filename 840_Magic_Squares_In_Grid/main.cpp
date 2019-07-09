#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    
    bool isMagicSquare(int i, int j, vector<vector<int>>& grid) {
        if (grid[i][j] != 5)
            return false;
        vector<int> unique(9, 0);
        for (int m = i - 1; m <= i + 1; m++) {
            for (int n = j - 1; n <= j + 1; n++) {
                if (grid[m][n] > 9 || grid[m][n] < 1)
                    return false;
                if (unique[grid[m][n] - 1])
                    return false;
                unique[grid[m][n] - 1] += 1;
            }
        }
        
        for (int m = i - 1; m <= i + 1; m++) {
            int sum = 0;
            for (int n = j - 1; n <= j + 1; n++) {
                sum += grid[m][n];
            }
            if (sum != 15)
                return false;
        }
        
        for (int n = j - 1; n <= j + 1; n++) {
            int sum = 0;
            for (int m = i - 1; m <= i + 1; m++) {
                sum += grid[m][n];
            }
            if (sum != 15)
                return false;
        }
        
        if ( (grid[i - 1][j - 1] + grid[i + 1][j + 1]) != 10)
            return false;
        if ( (grid[i + 1][j - 1] + grid[i - 1][j + 1]) != 10)
            return false;
        return true;
    }
    
    int numMagicSquaresInside(vector<vector<int>>& grid) {
        int count = 0;
        for (int i = 1; i < grid.size() - 1; i++) {
            for (int j = 1; j < grid[0].size() - 1; j++) {
                if (isMagicSquare(i, j, grid))
                    count++;
            }
        }
        return count;
    }
};

int main() {
    Solution* s = new Solution();
    vector<vector<int>> test{{4,3,8,4},{9,5,1,9},{2,7,6,2}};
    cout << s -> numMagicSquaresInside(test) << endl;
    return 0;
}