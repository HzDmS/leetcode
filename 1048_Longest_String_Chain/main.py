class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        maximum = 1
        words.sort(key=lambda x: len(x))
        hashmap = {word: 1 for word in words}
        for word in words:
            for i in range(len(word)):
                key = word[:i] + word[i + 1:]
                if key in hashmap:
                    hashmap[word] = max(hashmap[key] + 1, hashmap[word])
                    maximum = max(maximum, hashmap[word])
        return maximum
