#include<iostream>

using namespace std;

class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        std::vector<int> heap;
		for(auto row : matrix){
			for(auto item : row){
                if(heap.size() < k){
                    heap.push_back(item);
                    std::push_heap(heap.begin(), heap.end(), std::greater<int>());}
                else{
                    std::pop_heap(heap.begin(), heap.end(), std::greater<int>());
                    heap.pop_back();}
		}}
        return heap.front();
    }
};
