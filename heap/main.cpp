#include<iostream>
#include<vector>

using namespace std;

class KthLargest {
    
public:
    
    vector<int> heap;
    int size;
    
    KthLargest(int k, vector<int> &nums) {
        size = k;
        if(k > nums.size()){
            heap.insert(heap.begin(), nums.begin(), nums.end());
            std::make_heap(heap.begin(), heap.end(), std::greater<int>());
        }
        else{
            heap.insert(heap.begin(), nums.begin(), nums.begin() + size);
            std::make_heap(heap.begin(), heap.end(), std::greater<int>());
            for(std::vector<int>::iterator it = nums.begin() + size; it != nums.end(); ++it){add(*it);
            } 
        }
    }
    
    int add(int val) {
       if(heap.size() < size){
           heap.push_back(val);
           std::push_heap(heap.begin(), heap.end(), std::greater<int>());
       }else if(val > heap.front()){
           std::pop_heap(heap.begin(), heap.end(), std::greater<int>());
           heap.pop_back();
           heap.push_back(val);
           std::push_heap(heap.begin(), heap.end(), std::greater<int>());
       }
       return heap.front();
    }
};


void print_vector(vector<int> &nums){
    for(auto item : nums){
        cout << item << "\t";
    }
    cout << endl;
}


int main(){
    int arr[] = {5, 3, 4, 1, 2, 0};
    std::vector<int> nums(arr, arr + sizeof(arr) / sizeof(int));
    int k = 3;

    KthLargest test = KthLargest(k, nums);
    print_vector(test.heap);
    cout << test.add(10) << endl;
    
    return 0;
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
