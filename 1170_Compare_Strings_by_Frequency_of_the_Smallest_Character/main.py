class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        def func(word):
            minimum = "z"
            for char in word:
                if char < minimum:
                    minimum = char
            return word.count(minimum)
        
        ret = []
        
        q_list = [func(query) for query in queries]
        w_list = [func(word) for word in words]
        
        w_max = max(w_list)
        w_table = [0 for _ in range(w_max + 1)]
        for w in w_list:
            w_table[w - 1] += 1

        for i in range(w_max - 2, -1, -1):
            w_table[i] += w_table[i + 1]
        
        for q in q_list:
            if q >= w_max:
                ret.append(0)
            else:
                ret.append(w_table[q])
            
        return ret
                    
                    
