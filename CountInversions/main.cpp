#include<iostream>
#include<vector>

using namespace std;

template <class It>
int MergeSort(It first, It last, It scratch);

template <class It>
int Merge(It first, It mid, It last, It scratch);


int main() {

    vector<int> test {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
    vector<int> scratch(test.size(), 0);
    int res = MergeSort<vector<int>::iterator> (test.begin(), test.end() - 1, scratch.begin());
    cout << res << endl;

    for (auto it : scratch) {
        cout << it << " " ;
    }

    cout << endl;

    return 0;
}

template <class It>
int MergeSort(It first, It last, It scratch) {
    if (first == last) {
        return 0;
    }

    int res = 0;
    It mid = first, scratch_start = scratch;
    std::advance(mid, std::distance(first, last) / 2); 
    res += MergeSort(first, mid, scratch);
    std::advance(scratch, std::distance(first, mid));
    res += MergeSort(mid + 1, last, scratch + 1);

    res += Merge(first, mid, last, scratch_start);

    return res;
}

template <class It>
int Merge(It first, It mid, It last, It scratch) {
    int res = 0;
    It a = first, b = mid + 1, scratch_start = scratch;
    while (a <= mid && b <= last) {
       if (*a > *b) {
           res += mid - a + 1;
           *scratch++ = *b++;
       } else {
           *scratch++ = *a++;
       }
    }

    while (a <= mid) {
        *scratch++ = *a++;
    }
    
    while (b <= last) {
        *scratch++ = *b++;
    }

    while (first <= last) {
        *first++ = *scratch_start++; 
    }

    return res;
}
