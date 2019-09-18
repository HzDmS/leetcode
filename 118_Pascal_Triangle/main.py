class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        ans = [[1], [1, 1]]
        for i in range(2, numRows):
            tmp = [1]
            for j in range(1, i):
                tmp.append(ans[-1][j - 1] + ans[-1][j])
            tmp.append(1)
            ans.append(tmp)
        return ans
                
        
