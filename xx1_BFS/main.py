from collections import deque


class Solution(object):

    def findShortestPath(self, input_map):

        m, n = len(input_map), len(input_map[0])
        visited, q = set(), deque()

        length = 0
        q.append((0, 0))
        visited.add((0, 0))

        while q:

            for _ in range(len(q)):
                i, j = q.popleft()

                if input_map[i][j] == "X":
                    return length

                for direction in [[1, 0], [-1, 0], [0, 1], [0, -1]]:

                    new_i, new_j = i + direction[0], j + direction[1]

                    if new_i >= 0 and new_i < m and new_j >= 0 and new_j < n:
                        if input_map[new_i][new_j] != "D":
                            if (new_i, new_j) not in visited:
                                visited.add((new_i, new_j))
                                q.append((new_i, new_j))

            length += 1

        return length


if __name__ == "__main__":

    input_map = [['O', 'O', 'O', 'O'],
                 ['D', 'O', 'D', 'O'],
                 ['O', 'O', 'O', 'O'],
                 ['X', 'D', 'D', 'O']]

    s = Solution()
    print(s.findShortestPath(input_map))

