#include<iostream>

using namespace std;

class Test {
public:
    Test(std::string s) {
        for (char c : s) {
            cout << c << "\t";
        }
        cout << endl;
    }
};

int main() {
    int* a = nullptr;
    a = new int[10];

    Test t("\\//");

    for (int i = 0; i < sizeof(a) / sizeof(int); i++) {
        a[i] = i;
    }
    return 0;
}