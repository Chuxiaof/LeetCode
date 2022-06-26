class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        s = list(s)
        visited = [0] * len(s)
        groups = defaultdict(list)
        for pair in pairs:
            groups[pair[0]].append(pair[1]) 
            groups[pair[1]].append(pair[0])
            
        for idx in groups.keys():
            if not visited[idx]:
                tmp_idx = []
                self.dfs(idx, groups, visited, tmp_idx) 
                tmp_val = [s[i] for i in tmp_idx]
              
                tmp_idx = sorted(tmp_idx)
                tmp_val = sorted(tmp_val)
             
                for i in range(len(tmp_idx)):
                    s[tmp_idx[i]] = tmp_val[i]
        return ''.join(s)
        
            
    def dfs(self, idx, groups, visited, tmp_idx):
       
        if visited[idx]:
            return
        
        visited[idx] = 1
        tmp_idx.append(idx)
        for next_idx in groups[idx]:
            self.dfs(next_idx, groups, visited, tmp_idx)
            
            
        
                