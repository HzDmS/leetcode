class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s) // (2 * k)
        residual = len(s) - n * 2 * k
        i = 0
        while i < n:
            s[i * 2 * k: i * 2 * k + k] = s[i * 2 * k: i * 2 * k + k][::-1]
            i += 1
        if residual <= k:
            s[i * 2 * k: i * 2 * k + residual] = s[i * 2 * k: i * 2 * k + residual][::-1]
        else:
            s[i * 2 * k: i * 2 * k + k] = s[i * 2 * k: i * 2 * k + k][::-1]
        return "".join(s)

