class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        val = image[sr][sc]
        if val == color:
            return image
        self.dfs(image, sr, sc, val, color)
        return image

    def dfs(self, image, x, y, val, color):
        if x < 0 or y < 0 or x >= len(image) or y >= len(image[0]) or image[x][y] != val:
            return
        image[x][y] = color
        self.dfs(image, x-1, y, val, color)
        self.dfs(image, x+1, y, val, color)
        self.dfs(image, x, y-1, val, color)
        self.dfs(image, x, y+1, val, color)
