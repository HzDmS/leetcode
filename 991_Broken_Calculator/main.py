class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        
        # the program starts from Y
        # if Y is even, then Y //= 2
        # else Y = Y + 1, then Y // 2
        # when Y is smaller than X, then decrease X by 1 recursively until X == Y
        
        total = 0
        
        while not X == Y:
            
            if Y > X:
                if Y % 2 == 0:
                    Y //= 2
                    total += 1
                else:
                    Y += 1
                    Y //= 2
                    total += 2
            else:
                total += (X - Y)
                Y = X
        
        return total
