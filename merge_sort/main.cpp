#include<iostream>
#include<vector>
#include<random>
#include <chrono>

using namespace std;
using namespace std::chrono;

class MergeSort{
    public:
        //MergeSort();
        void merge(vector<int>& arr, int l, int m, int r);
        void mergeSort(vector<int>& arr, int l, int r);
        void printArray(vector<int>& arr) {
            for(unsigned long i = 0; i < arr.size(); i++){
                cout << arr[i] << ", ";
            }
            cout << endl;
        }
        vector<int> generateRandomVector(int num, int min, int max);
        //~MergeSort();
};

int main(){

    MergeSort m = MergeSort();
    vector<int> array = m.generateRandomVector(10000, 0, 1000);
    high_resolution_clock::time_point t1 = high_resolution_clock::now();
    m.mergeSort(array, 0, array.size() - 1);
    high_resolution_clock::time_point t2 = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>( t2 - t1 ).count();
    cout << "running time: " << duration << endl;
    return 0;
}

void MergeSort::mergeSort(vector<int>& arr, int l, int r){
    if (l < r){
        int m = (l + r) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

void MergeSort::merge(vector<int>& arr, int l, int m, int r){
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;
    int left[n1], right[n2];
    for(i = 0; i < n1; i++) {
        left[i] = arr[l + i];
    }
    for(j = 0; j < n2; j++) {
        right[j] = arr[m + 1 + j];
    }
    
    i = j = k = 0;
    
    while(i < n1 && j < n2){
        if(left[i] < right[j]) {
            arr[l + k] = left[i];
            i++;
        } else {
            arr[l + k] = right[j];
            j++;
        }
        k++;
    }

   while(i < n1) {
       arr[l + k] = left[i];
       i++;
       k++;
   } 

   while(j < n2) {
       arr[l + k] = right[j];
       j++;
       k++;
   }
}

vector<int> MergeSort::generateRandomVector(int num, int min, int max) {
    std::random_device rd; 
    std::mt19937 gen(rd()); // these can be global and/or static, depending on how you use random elsewhere

    std::vector<int> values(num); 
    std::uniform_int_distribution<> dis(min, max);
    std::generate(values.begin(), values.end(), [&](){ return dis(gen); });
    return values; 
}
