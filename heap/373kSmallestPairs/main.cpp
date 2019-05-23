#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    
//     vector<pair<int, int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        
//         vector<pair<int, int>> res;
        
//         auto comp = [](const pair<int, int> &a, const pair<int, int> & b) {
//             return (a.first + a.second) < (b.first +b.second); 
//         };
//         priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(comp)> q(comp);
//         for(int i : nums1){
//             for(int j : nums2){
//                 if(q.size() < k){
//                     q.push(make_pair(i, j));
//                 }else{
//                     pair<int, int> top = q.top();
//                     if( (i + j) < top.first + top.second) {
//                         q.pop();
//                         q.push(make_pair(i, j));
//                     }
//                 }
//             }
//         }
//         while(!q.empty()){
//             res.push_back(q.top());
//             q.pop();
//         }
//         return res;
//     }
    
        vector<pair<int, int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        vector<pair<int, int>> res;
        int i = 0; int j = 0;
        while(res.size() < k && i < nums1.size() && j < nums2.size()) {
            res.push_back(make_pair(nums1[i], nums2[j]));
            if(nums1[i + 1] + nums2[j] > nums2[j + 1] + nums1[i]){
                j++;
            }else{
                i++;
            }
        }
        return res;
    }
};

int main(){
	Solution s;
	vector<int> a({1, 7, 11});
	vector<int> b({2, 4, 6});
	vector<pair<int, int>> output = s.kSmallestPairs(a, b, 3);
	for(auto item : output) {
        cout << "(" << item.first << ", " << item.second << ")" << endl;
    }
    return 0;
}
