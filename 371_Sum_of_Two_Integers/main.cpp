#include <iostream>

using namespace std;

int count_ones(int n);
int Add(int x, int y);
uint32_t reverseBits(uint32_t n);

int main() {
    //count ones in an integer's binary representation.
    int num = 12345;
    cout << "count ones of " << num << ": "
         << count_ones(num) << endl;

    //perform Addation without '+'
    int a = 9, b = 5;
    cout << "sum of " << a << " and " << b << ": "
         << Add(a, b) << endl;

    uint32_t x = 12345;
    cout << std::bitset<32>(x) << endl;
    cout << std::bitset<32>(reverseBits(x)) << endl;

    return 0;
}

int count_ones(int n) {
    int count = 0;
    while (n) {
        n = n & (n - 1);
        count++;
    }
    return count;
}

int Add(int x, int y) {
    int carry = 0;
    while(y) {
        carry = x & y;
        x = x ^ y;
        y = carry << 1;
    }
    return x;
}

uint32_t reverseBits(uint32_t n) {
    uint32_t mask = 1 << 31, res = 0;
    for (int i = 0; i < 32; i++) {
        if (n & 1) {
            res |= mask;
        }
        n >>= 1;
        mask >>= 1;
    }
    return res;
}