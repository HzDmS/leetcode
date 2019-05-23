#include<iostream>

using namespace std;

int main(){
    string s = "this";
    cout << s << endl;
    sort(s.begin(), s.end());
    cout << s << endl;
    string a(s);
    cout << a << endl;
    return 0;
}
