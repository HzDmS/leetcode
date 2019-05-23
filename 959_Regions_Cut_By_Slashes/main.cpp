#include<iostream>
#include<string>
#include<vector>

using namespace std;

class Table {
public:
    int* parent = nullptr;
    int size;

    Table(int size){
        this -> size = size;
        parent = new int[size];
        for (int i = 0; i < size; i++) {
            parent[i] = i;
        }
    }
    
    void join(int m, int n){
        parent[find(m)] = find(n);
    }

    int find(int x){
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
};

class Solution {
public:
    int regionsBySlashes(vector<string>& grid) {
        
        int res = 0;
        
        int n = grid.size();
        Table tab(4 * n * n);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int base = 4 * (n * i + j);
                if (grid[i][j] != '\\') {
                    tab.join(base, base + 1);
                    tab.join(base + 2, base + 3);
                }
                if (grid[i][j] != '/') {
                    tab.join(base, base + 2);
                    tab.join(base + 1, base + 3);
                }
                if (i > 0) {
                    tab.join(base, base - 4 * n + 3);
                }
                if (j > 0) {
                    tab.join(base + 1, base - 4 + 2);
                }
            }
        }
        
        for (int i = 0; i < tab.size; i++){
            if (tab.parent[i] == i) {
                res++;
            }
        }
        
        return res;
        
    }
};

int main () {
    vector<string> grid({"\\/", "/\\"});
    Solution s;
    cout << s.regionsBySlashes(grid) << endl;
    return 0;
}