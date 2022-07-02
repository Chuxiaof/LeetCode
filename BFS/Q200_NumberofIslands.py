class Solution:
    # approach1: DFS
    # Time: O(nm)
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    ans += 1
                    self.dfs(grid, i, j)

        return ans

    def dfs(self, grid, x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == '0':
            return
        grid[x][y] = '0'
        self.dfs(grid, x-1, y)
        self.dfs(grid, x+1, y)
        self.dfs(grid, x, y-1)
        self.dfs(grid, x, y+1)

    # approach2: BFS
    # Time: O(mn)
    DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        ans = 0
        visited = set()
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == "1" and (m, n) not in visited:
                    self.bfs(grid, m, n, visited)
                    ans += 1

        return ans

    def bfs(self, grid, x, y, visited):
        queue = collections.deque([(x, y)])
        visited.add((x, y))
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in DIRECTIONS:
                next_x, next_y = x + delta_x, y + delta_y
                if not self.is_valid(grid, next_x, next_y, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))

    def is_valid(self, grid, x, y, visited):
        if (x, y) in visited:
            return False
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        return grid[x][y] == "1"
