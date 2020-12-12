import random

random.seed(42)


class Codec:
    
    char_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHJIKLMNOPQRSTUVWXYZ0123456789"
    k = 8
    
    def __init__(self):
        self.dict = {}
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        shortUrl = "https://tinyurl.com/" + "".join(random.choices(self.char_set, k=self.k))
        self.dict[shortUrl] = longUrl
        return shortUrl
        
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.dict[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
