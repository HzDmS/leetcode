class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        
#         hashmap = {}
        
#         def dfs(cur):
#             cost = sum([x * y for x, y in zip(price, cur)])
#             for offer in special:
#                 new = tuple([x - y for x, y in zip(cur, offer[:-1])])
#                 if min(new) >= 0:
#                     cost = min(cost, offer[-1] + hashmap.get(new, dfs(new)))
#             hashmap[cur] = cost
#             return cost

#         return dfs(tuple(needs))

        stack, hashmap, minimal = [], {}, sum([x * y for x, y in zip(price, needs)])
        key = tuple(needs)
        stack.append(key)
        hashmap[key] = 0
        
        while stack:
            cur = stack.pop()
            for offer in special:
                new = tuple([x - y for x, y in zip(cur, offer[:-1])])
                minimal = min(minimal, hashmap[cur] + sum([x * y for x, y in zip(price, cur)]))
                if min(new) >= 0:
                    cost = hashmap[cur] + offer[-1]
                    if cost < minimal:
                        if not new in hashmap:
                            hashmap[new] = hashmap[cur] + offer[-1]
                        else:
                            hashmap[new] = min(hashmap[cur] + offer[-1], hashmap[new])
                        stack.append(new)
        return minimal
