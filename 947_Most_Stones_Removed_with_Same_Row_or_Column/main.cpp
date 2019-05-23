#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    
    class UnionFind{
    public:
        int* parent;
        int size;
        UnionFind(int size) {
            this -> size = size;
            parent = new int[size];
            for (int i = 0; i < size; i++) {
                parent[i] = i;
            }
        }
        
        int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }
        
        void join(int m, int n) {
            parent[find(n)] = find(m);
        }
    };
    
    int removeStones(vector<vector<int>>& stones) {
        
        int count;
        
        int n = stones.size();
        UnionFind uf(n);
        
        for (int i = 0; i < n - 1; i++) {
            for(int j = i + 1; j < n; j++) {
                if (isConnected(stones[i], stones[j])) {
                    uf.join(i, j);
                }
            }
        }
        
        for (int i = 0; i < uf.size; i++) {
            if (uf.parent[i] == i) {
                count++;
            }
        }
        
        return n - count;
        
    }
    
    bool isConnected(vector<int>& a, vector<int>& b) {
        if (a[0] == b[0] || a[1] == b[1]) return true;
        return false;
    }
};

int main() {
    Solution s;
    vector<vector<int>> stones({{0, 0}, {0, 2}, {1, 1},
                                {2, 0}, {2, 2}});
    cout << s.removeStones(stones) << endl;
    return 0;
}