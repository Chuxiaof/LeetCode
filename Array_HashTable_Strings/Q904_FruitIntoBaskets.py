class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count, i, j, ans = {}, 0, 0, 0
        tree = fruits
        for idx, v in enumerate(tree):
            count[v] = count.get(v, 0) + 1
            while len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0: del count[tree[i]]
                i += 1    
            
            ans = max(ans, j-i+1)
            j += 1
            
        return ans
                