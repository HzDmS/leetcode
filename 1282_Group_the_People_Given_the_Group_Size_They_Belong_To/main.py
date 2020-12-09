class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        gdict, res = {},  []
        for i, gsize in enumerate(groupSizes):
            if gsize not in gdict:
                gdict[gsize] = []
            gdict[gsize].append(i)
            if len(gdict[gsize]) == gsize:
                res.append(gdict.pop(gsize))
        return res

