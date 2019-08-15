class Solution:
    """
    @param stringIn: The original string.
    @param K: The length of substrings.
    @return: return the count of substring of length K and exactly K distinct characters.
    """
    def KSubstring(self, stringIn, K):
        # Write your code here
        
        if K > len(stringIn):
            
            return 0
            
        ret = set()
            
        hashmap = {}
        cur_len = 0
        for i in range(K):
            if stringIn[i] not in hashmap:
                hashmap[stringIn[i]] = 0
                cur_len += 1
            hashmap[stringIn[i]] += 1
        
            if cur_len == K:
                ret.add(stringIn[0 : K])
        
        for i in range(K, len(stringIn)):
            
            hashmap[stringIn[i - K]] -= 1
            
            if hashmap[stringIn[i - K]] == 0:
                cur_len -= 1
            
            if stringIn[i] not in hashmap or hashmap[stringIn[i]] == 0:
                cur_len += 1
                hashmap[stringIn[i]] = 0
            hashmap[stringIn[i]] += 1
            if cur_len == K:
                ret.add(stringIn[i - K + 1: i + 1])
            
        return len(ret)
