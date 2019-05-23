#include<iostream>
#include<vector>

using namespace std;


class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> empty;
        vector<int> path;
        
        vector<vector<int>> graph(numCourses);
        for (auto row : prerequisites) {
            graph[row[1]].push_back(row[0]);
        }
        
        vector<bool> visited(numCourses, false);
        vector<bool> inRecursion(numCourses, false);
        
        for (int i = 0; i < numCourses; i++) {
            if (!visited[i] &&
                !isAcyclic(graph, visited, inRecursion, i, path)) {
                return empty;
            }
        }
        reverse(path.begin(), path.end());
        return path;
    }
    
    bool isAcyclic(vector<vector<int>> &graph,
                   vector<bool> &visited,
                   vector<bool> &inRecursion,
                   int v,
                   vector<int>& path){
        if (inRecursion[v]) return false;
        if (visited[v]) return true;
        
        visited[v] = inRecursion[v] = true;
        
        for (int i : graph[v]) {
            if (!isAcyclic(graph, visited, inRecursion, i, path))
                return false;
        }
        path.push_back(v);
        inRecursion[v] = false;
        return true;
    }
    
};

int main(){
    Solution s;
    vector<vector<int>> edges{{0, 1}};
    int numCourses = 2;
    vector<int> res = s.findOrder(numCourses, edges);
    cout << "shit" << endl;
    return 0;
}
