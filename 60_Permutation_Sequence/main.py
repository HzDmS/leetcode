class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fac = [1]
        for i in range(1, n):
            fac.append(fac[-1] * i)
        per = []
        digits = [*range(1, n + 1)]
        for i in range(n):
            idx = (k - 1) // fac[n - i - 1]
            per.append(digits[idx])
            digits.pop(idx)
            k = k % fac[n - i - 1]
        return "".join(list(map(str, per)))

