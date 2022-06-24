class Solution:
    # approach1: dfs
    # Time: O(n)
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0] * len(rooms)
        visited[0] = 1
        for key in rooms[0]:
            self.dfs(rooms, key, visited)
        return sum(visited)==len(rooms)
                
    def dfs(self, rooms, key, visited):
        if visited[key]: return
        visited[key] = 1
        for k in rooms[key]:
            self.dfs(rooms, k, visited)


    # approach2: bfs
    # Time: O(n)
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True
        queue = deque(rooms[0])
        while(queue):
            key = queue.popleft()
            if not visited[key]:
                visited[key] = 1
                queue.extend(rooms[key])
            
        return all(visited)
            
        