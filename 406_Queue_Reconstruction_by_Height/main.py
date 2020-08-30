class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort()
        n = len(people)
        positions = list(range(n))
        queue = [[0, 0]] * n
        prev, identicals = -1, 0
        for height, count in people:
            if height == prev:
                identicals += 1
                i = count - identicals
            else:
                i = count
                identicals = 0
            position = positions[i]
            positions.pop(i)
            queue[position] = [height, count]
            prev = height
        return queue

