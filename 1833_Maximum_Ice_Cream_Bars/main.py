class Solution:
    
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for i, cost in enumerate(costs):
            coins -= cost
            if coins < 0:
                return i
        return len(costs)

