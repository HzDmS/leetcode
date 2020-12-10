class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: point[0])
        width = 0
        for i in range(1, len(points)):
            width = max(width, points[i][0] - points[i - 1][0])
        return width

