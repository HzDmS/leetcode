#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    
    class UnionFind{
    public:
        int* friend_circle = nullptr;
        int size = 0;
        
        UnionFind(int size) {
            this -> size = size;
            friend_circle = new int[size];
            for (int i = 0; i < size; i++) {
                friend_circle[i] = i;
            }
        }
        
        int find(int x) {
            if (friend_circle[x] != x) {
                friend_circle[x] = find(friend_circle[x]);
            }
            return friend_circle[x];
        }
        
        void join(int m, int n) {
            friend_circle[find(n)] = find(friend_circle[m]);
        }
        
    };
    
    int findCircleNum(vector<vector<int>>& M) {
        
        int res = 0;
        
        int n = M.size();
        UnionFind uf(n);
        
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (M[i][j]) {
                    uf.join(i, j);
                }
            }
        }
        
        for (int i = 0; i < n; i++) {
            if (uf.friend_circle[i] == i) {
                res++;
            }
        }
        
        return res;
        
    }
    
};

int main() {

    vector<vector<int>> m({{1, 0, 0, 1},
                           {0, 1, 1, 0},
                           {0, 1, 1, 1},
                           {1, 0, 1, 1}});
    
    Solution s;
    cout << s.findCircleNum(m) << endl;

    return 0;
}