class Solution:
    # approach 1
    # time complexity O(nn)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected : 
            return 0
        
        ans = 0
        for curr in range(len(isConnected)):
                if isConnected[curr][curr] == 1:
                    ans += 1
                    self.dfs(isConnected, curr)
                    
        return ans


    def dfs(self, isConnected, curr):
        for x in range(len(isConnected)):
            if isConnected[curr][x]:
                isConnected[curr][x] = 0
                isConnected[x][curr] = 0
                self.dfs(isConnected, x)



    # approach 2:
    # time complexity O(nn)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected : 
            return 0
    
        ans = 0
        visited = [0] * len(isConnected)
        for curr in range(len(isConnected)):
                if not visited[curr]:
                    ans += 1
                    
                    self.dfs(isConnected, curr, visited)
                
        return ans
                    
    def dfs(self, isConnected, curr, visited):
        visited[curr] = 1
        for x in range(len(isConnected)):
            if isConnected[curr][x] and not visited[x]:
                self.dfs(isConnected, x, visited)
                
                
            