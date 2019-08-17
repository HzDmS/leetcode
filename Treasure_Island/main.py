class Solution(object):

    def findShortestPath(self, input_map):

        """
        Parameters
        ----------
        input_map: 2D list.

        Returns
        -------
        length: int, length of shortest path.
        """
        m, n = len(input_map), len(input_map[0])
        visited = [[False for i in range(n)] for j in range(m)]
        length = 0
        paths = []

        def bfs(row, col, length, paths, visited, input_map):

            if row == m or row < 0 or col == n or col < 0 or visited[row][col]:
                return

            if input_map[row][col] == 'D':
                return

            if input_map[row][col] == 'X':
                paths.append(length)
                return

            visited[row][col] = True
            bfs(row + 1, col, length + 1, paths, visited, input_map)
            bfs(row - 1, col, length + 1, paths, visited, input_map)
            bfs(row, col + 1, length + 1, paths, visited, input_map)
            bfs(row, col - 1, length + 1, paths, visited, input_map)
            visited[row][col] = False

        bfs(0, 0, length, paths, visited, input_map)

        shortest = float('inf')
        for path in paths:
            shortest = min(shortest, path)

        return shortest


if __name__ == "__main__":

    input_map = [['O', 'O', 'O', 'O'],
                 ['D', 'O', 'D', 'O'],
                 ['O', 'O', 'O', 'O'],
                 ['X', 'D', 'D', 'O']]

    s = Solution()
    print(s.findShortestPath(input_map))

