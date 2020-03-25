class Solution:
    def myAtoi(self, str: str) -> int:
        res, sign = 0, 1
        flag = False
        i = 0
        n = len(str)
        while i < n:
            if not flag:
                if str[i] == " ":
                    i += 1
                    continue
                else:
                    flag = True
                    if str[i] == "-":
                        sign = -1
                        i += 1
                    elif str[i] == "+":
                        i += 1
                    else:
                        pass
                    if i < n and not str[i].isdigit():
                        return 0
            else:
                if str[i].isdigit():
                    if res < 2 ** 31:
                        res = res * 10 + int(str[i])
                        i += 1
                    else: break
                else: break
        if sign > 0:
            return res if res < 2 ** 31 else 2 **31 - 1
        else:
            return sign * res if res < 2 ** 31 else -2 ** 31

