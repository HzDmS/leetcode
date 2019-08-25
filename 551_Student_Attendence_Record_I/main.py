class Solution:
    def checkRecord(self, s: str) -> bool:
        
        left, right = 0, 0
        cnt_a = 0
        
        for char in s:
            if char == "A":
                cnt_a += 1
                right += 1
                left = right
            elif char == "P":
                right += 1
                left = right
            else:
                right += 1
            
            if right - left > 2 or cnt_a > 1:
                return False
            
        return True
