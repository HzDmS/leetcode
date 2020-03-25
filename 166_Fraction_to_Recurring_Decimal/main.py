class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = ""
        if numerator / denominator < 0:
            res += "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        res += str(numerator // denominator)
        numerator %= denominator
        if numerator:
            res += "."
        else:
            return res
        repeat, i = {}, len(res)
        while numerator:
            if numerator not in repeat:
                repeat[numerator] = i 
                numerator *= 10
                res += str(numerator // denominator)
                numerator %= denominator 
                i += 1
            else:
                pos = repeat[numerator]
                res = res[:pos] + "(" + res[pos:] + ")"
                return res
        return res

