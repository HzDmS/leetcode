#include<iostream>
#include <type_traits>

using namespace std;

const std::string testString("test!");
const std::string* str_ptr = &testString;

constexpr int i = 0;
constexpr const int* j = &i;

void f() {
    static int x = 0;
    cout << x++ << endl; 
}

int main() {
    for (int i = 0; i < 10; i++) {
        f();
    }
    return 0;
}