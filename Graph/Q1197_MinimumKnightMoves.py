TRADEOFF = [(1, 2), (2, 1), (2, -1), (1, -2),
                   (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == y == 0:
            return 0
        queue = collections.deque([(0, 0)])
        distances = {(0, 0) : 0}
        while queue:
            curr_x, curr_y = queue.popleft()
            if (curr_x, curr_y) == (x, y):
                    return distances[(curr_x, curr_y)]
                
            for delta_x, delta_y in TRADEOFF:
                next_x = curr_x + delta_x
                next_y = curr_y + delta_y
                if (next_x, next_y) in distances:
                    continue
                queue.append((next_x, next_y))
                distances[(next_x, next_y)] = distances[(curr_x, curr_y)] + 1
                