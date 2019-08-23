class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = []
        n = len(rooms)
        room_set = set([x for x in range(n)])
        
        room_set.remove(0)
        stack.extend(rooms[0])
        
        while stack:
            for _ in range(len(stack)):
                key = stack.pop()
                if key in room_set:
                    room_set.remove(key)
                    stack.extend(rooms[key])
        
        if room_set:
            return False
        return True
