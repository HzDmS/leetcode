class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i = 0
        while i < len(gas):
            tmp = self.canComeBack(i, gas, cost)
            if tmp < 0:
                return i
            elif tmp > i:
                i = tmp
            else:
                return -1
        return -1
        
    def canComeBack(self, start, gas, cost):
        l = len(gas)
        tank = gas[start] - cost[start] 
        for i in range(1, l + 1):
            cur = (start + i) % l
            if tank < 0:
                return cur
            else:
                tank = tank + gas[cur] - cost[cur]
        return -1

