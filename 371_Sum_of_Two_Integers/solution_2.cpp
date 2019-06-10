class Solution {
public:
    // explaination:
    //     a ^ b is the bit sum without adding the carry.
    //     a & b is the carry bits.
    //     the carry bits need to be shifted to the left side for one bit.
    //     but there is a risk that the carry bits represent a negative number.
    //     The solution is to use INT_MAX as a mask, as the highest bit of the
    //     carry bits will not be used.
    //     Perform the binary addition until carry bits is equal to zero.
    
    int getSum(int a, int b) {
        auto t = INT_MAX & (a & b);
        return b ? getSum(a^b, t<<1) : a;
    }
};
