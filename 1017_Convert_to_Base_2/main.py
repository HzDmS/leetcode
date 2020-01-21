class Solution:
    def baseNeg2(self, N: int) -> str:
        
        if N == 0:
            return "0"
        
        res = []
        flag = 1
        while N > 0:
            r = N % 2
            res.append(str(r))
            if flag:
                N = (N - r) // 2
            else:
                N = (N + r) // 2
            flag = 1 - flag
        res.reverse()
        return "".join(res)

