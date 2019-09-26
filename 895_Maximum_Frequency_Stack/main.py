class FreqStack:

    def __init__(self):
        self.stack = []
        self.cnt = {}
        self.top = 0


    def push(self, x: int) -> None:
        if x not in self.cnt:
            self.cnt[x] = 0
        self.cnt[x] += 1
        if self.cnt[x] > len(self.stack):
            self.stack.append([x])
            self.top = self.cnt[x]
        else:
            self.stack[self.cnt[x] - 1].append(x)


    def pop(self) -> int:
        cur = self.stack[-1]
        ret = cur.pop()
        if not cur:
            self.stack.pop()
        self.cnt[ret] -= 1
        return ret
