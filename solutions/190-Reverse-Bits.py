'''
190. Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

Example 1:
    Input: 00000010100101000001111010011100
    Output: 00111001011110000010100101000000
    Explanation: The input binary string 00000010100101000001111010011100
    represents the unsigned integer 43261596, so return 964176192 which its
    binary representation is 00111001011110000010100101000000.
'''
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        num = 0
        for i in xrange(32):
            if (n >> i) & 1:
                num += ((n >> i) & 1) << (31 - i)
        return num
            
