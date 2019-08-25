from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        hash_map = Counter(chars)
        
        def check(word):
            local_map = Counter(word)
            for k in local_map.keys():
                if not k in hash_map or hash_map[k] < local_map[k]:
                    return False
            
            return True
        
        ret = 0
        
        for word in words:
            if check(word):
                ret += len(word)
                
        return ret
