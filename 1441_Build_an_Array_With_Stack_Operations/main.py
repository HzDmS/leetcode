class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i, j = 0, 1
        output = []
        while i < len(target):
            output.append("Push")
            if j < target[i]:
                output.append("Pop")
            else:
                i += 1
            j += 1
        return output
                
