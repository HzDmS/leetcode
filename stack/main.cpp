#include<iostream>
#include "stack.h"

using namespace std;

int main() {
    Stack s(10);
    for (int i = 0; i < 20; i++) {
        s.push(i);
        cout << "top: " << s.top() << "\tsize: " << s.size() << endl;
    }

    for (int i = 0; i < 20; i++) {
        cout << "pop: " << s.pop() << "\tsize:" << s.size() << endl; 
    }
    
    return 0;
}